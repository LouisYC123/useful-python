# %%
import pandas as pd
from typing import Literal


df = pd.DataFrame(
    {
        "dept": [
            "finance",
            "human_resources",
            "sales",
            "insurance",
            "data",
            "engineering",
            "marketing",
        ],
        "remediation": [5, 6, 7],
    }
)


# %%
Literal[
    "finance",
    "human_resources",
    "sales",
    "insurance",
    "data",
    "engineering",
    "marketing",
]


def create_total_spend_column(df, target_calc: str) -> pd.DataFrame:
    """Provides 'Total' columns for each target set of columns in target_calc."""
    target_cols = [col for col in df.columns if target_calc in col]
    df[f"Total {target_calc}"] = df[target_cols].sum(axis=1)
    return df


# create_totals_column(df, "test")

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


# ============================== Write up
"""
Here we have a funciton that sums costs for particular domain-specific aspects of a business, allowing a user to 
choose which department they want to total costs for.


the benefits of enums are:
1. You cannot accidentally create an enum with the wrong value
2. You can easily access all the values in the enum
3. You can clearly communicate how your function should be used
4. You can define the enum clearly at the top of a script or in a seperate ‘settings.py’ module, which makes it readily accessible and maintainable




furthermore, it prevents you from repeating yourself...
... but lets say we had another function that also required users to choose from this list, 
you would have to write these out inside Literal again. Now if you wanted to update this list,
you have to do it in multiple places.
"""
