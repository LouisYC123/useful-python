# -----------------------------------------------------------------------------
#  ---- Find overlapping records (overlapping dates)
import pandas as pd

"""Two functions to help identify records with overlapping start and end dates
"""


def _add_overlapping_id(
    df: pd.DataFrame,
    id_var: str,
    left: str,
    right: str,
    closed: str,
) -> pd.DataFrame:
    """Helper function used for add overlapping_group_id
    Used to identify/mark overlapping intervals with two new columns,

    "overlapping_group_id", and "is_overlapping".

    Intervals that overlap with any interval have "is_overlapping" as True

    Args:
        df: Input dataframe
        id_var: column to assign the 'overlapping_id' from
        left: column that contains the left bound
        right: column that contains the right bound
        closed: what type of interval is this?

    Returns:
        `df` with additional columns 'overlapping_id' and 'is_overlapping'
            added
    """

    if closed == "both":
        entry_sort_tweak = -1
    elif closed == "left":
        entry_sort_tweak = 1
    else:
        entry_sort_tweak = 0

    dimension = (
        df[[id_var, left, right]]
        .melt(id_vars=id_var, ignore_index=False, var_name="side", value_name="time")
        .assign(
            _direction=lambda df: df.side.map({right: -1, left: 1}),
            _sort_tweak=lambda df: df.side.map({right: 0, left: entry_sort_tweak}),
        )
        .sort_values(["time", "_sort_tweak", id_var], ascending=True)
        .assign(cumsum=lambda row: row["_direction"].cumsum())
        .reset_index(drop=True)
    )

    overlap_index = [
        list(
            set(dimension.iloc[idx[0] : idx[1]][id_var].tolist())
        )  # a list of lists containing original index values between entry point and exit point
        for idx in [
            [st, ed]  # start row, end row
            for st, ed in zip(
                # index values on column cumsum with value 1 and
                # column variable with value 1. this represents the entry point
                dimension[
                    (dimension["cumsum"] == 1) & (dimension["_direction"] == 1)
                ].index.tolist(),
                # index values on column cumsum with value 0. this represents the exit point
                dimension[dimension["cumsum"] == 0].index.tolist(),
            )
            if st + 1 != ed  # remove adjacent numbers as they represent the same record
        ]
    ]

    df = df.assign(is_overlapping=False, overlapping_id=df[id_var])

    for i in overlap_index:
        rows = df.index.isin(i)
        df.loc[rows, "overlapping_id"] = min(i)
        df.loc[rows, "is_overlapping"] = True

    return df


def add_overlapping_group_id(
    df: pd.DataFrame,
    grouping_cols: str = "employee_code",
    interval_col: str = "interval",
):
    """Used to identify/mark overlapping intervals within a group. Returns `df`
    with two new columns: "overlapping_group_id", and "is_overlapping".

    All rows with the same "Overlapping_group_id" are in the same "overlapping"
    group, i.e. all intervals withing that group overlap with at least one other
    interval in that group.

    Intervals that overlap with any interval have "is_overlapping" as True

    Args:
        df: Input dataframe
        grouping_cols: Columns to group intervals by - only intervals with the
            same value of "grouping_cols" can overlap with eachother.

    Returns:
        `df` with additional columns 'overlapping_group_id' and 'is_overlapping'
            added

    """
    # grouping_cols = col_spec.prep_col_spec(col_spec=grouping_cols, df=df).to_list()
    grouping_cols = grouping_cols.to_list()

    df = (
        df.copy()
        .reset_index(drop=True)
        .assign(
            _interval_id=np.arange(len(df)),
            _left=df[interval_col].array.left,
            _right=df[interval_col].array.right,
        )
    )

    closed = df[interval_col].array.closed

    result = (
        df.groupby(grouping_cols, group_keys=False, observed=True)
        .apply(
            _add_overlapping_id,
            id_var="_interval_id",
            left="_left",
            right="_right",
            closed=closed,
        )
        .drop(columns=["_interval_id", "_left", "_right"])
        .rename(columns={"overlapping_id": "overlapping_group_id"})
    )

    return result


# -----------------------------------------------------------------------------
#  ---- Read multiple files and concat into single df
import pandas as pd
import glob
import os

path = "/home/project/my_folder"
all_files = glob.glob(os.path.join(path, "*Timesheet*.csv"))


datasets = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None)
    datasets.append(df)

data = pd.concat(datasets, ignore_index=True)

# -----------------------------------------------------------------------------
# ---- Use pd.Grouper to sum values in bins
"""
FY to be calculated from 1 July - 30 June the following year. 
The determination of FY will be the "End Date" of the pay period (column I). 
"""
var = (
    df.groupby(
        [pd.Grouper(key="payslip_end", freq="BAS-JUL", closed="left"), "employee_code"]
    )
    .variance_with_setoff.sum()
    .reset_index()
    .rename(columns={"payslip_end": "FY_End"})
)

# -----------------------------------------------------------------------------
# ---- Use tranform() and groupby to add a col that sums per group (like a sql window function)

df["total_remediation"] = df.groupby("employee_code").variance_with_setoff.transform(
    "sum"
)

# -----------------------------------------------------------------------------
# ---- Use map() to check if a target (e.g - Employee) has a particular value in any of its rows

df["has_Workday"] = df["Employee ID"].map(
    df.groupby("Employee ID").apply(lambda x: x["source"].eq("Workday").any())
)

# -----------------------------------------------------------------------------
# --- Conditional assign a value from another column to a newly created column

df["new_col"] = df.apply(
    lambda row: row["col_of_interest"] if row["source"] == "Workday" else None,
    axis=1,
)

# -----------------------------------------------------------------------------
# --- Using Forward fill

df["col_1"] = df["col_1"].fillna(method="ffill")


# -----------------------------------------------------------------------------
# --- Using np.select

import numpy as np

choices = [df["use_this_col"]]
conditions = [df["if_this_col"] == True]
default_value = df["default_to_this_col"]
df["create_this_col"] = np.select(conditions, choices, default=default_value)


# -----------------------------------------------------------------------------
# --- Split a string into multiple columns
df[["break_start", "break_end"]] = df.UnpaidBreaks.str.split("=>", 1, expand=True)


# -----------------------------------------------------------------------------
# --- Open and read a SQL script
sql_script_path = "my+path"
fd = open(f"{sql_script_path}get_card_data.sql", "r")
get_card_data_SQL = fd.read()
fd.close()
