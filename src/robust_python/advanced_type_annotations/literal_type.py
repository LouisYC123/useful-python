# %%
import pandas as pd
from typing import Literal


df = pd.DataFrame({"empCode": [1, 2, 3], "remediation": [5, 6, 7]})


def create_totals_column(
    df, target_calc: Literal["remediation", "interest", "tax"]
) -> pd.DataFrame:
    """Provides 'Total' columns for each target set of columns in target_calc."""
    target_cols = [col for col in df.columns if target_calc in col]
    df[f"Total {target_calc}"] = df[target_cols].sum(axis=1)
    return df


create_totals_column(df, "test")

"""
Running mypy, we get the following error
"""

"""
literal_type.py:37: 
error: Argument 2 to "create_totals_column" has incompatible type 
"Literal['test']"; expected "Literal['remediation', 'interest', 'tax']"  
[arg-type]
"""
# %%
from typing import Optional


def calculate_rate_bonus(number_of_franchises: Optional[int] = None):
    return number_of_franchises * 1.10
