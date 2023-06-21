# %%
import pandas as pd
from typing import Literal


df = pd.DataFrame(
    {
        "finance_payroll": [3, 35, 46, 7],
        "finance_rent": [3, 15, 26, 37],
        "finance_electricity": [3, 55, 65, 67],
        "human_resources_payroll": [3, 55, 6, 7],
        "human_resources_rent": [34, 55, 63, 7],
        "human_resources_electricity": [3, 25, 6, 67],
        "sales_payroll": [33, 51, 66, 77],
        "sales_rent": [3, 25, 61, 72],
        "sales_electricity": [3, 15, 96, 7],
        "data_analytics_payroll": [3, 62, 6, 39],
        "data_analytics_rent": [3, 5, 12, 47],
        "data_analytics_electricity": [53, 35, 6, 72],
    }
)
df

# %%


# def create_total_spend_column(
#     df: pd.DataFrame,
#     target_department: Literal[
#         "finance",
#         "human_resources",
#         "sales",
#         "insurance",
#         "data",
#         "engineering",
#         "marketing",
#     ],
# ) -> pd.DataFrame:
#     """Sums columns for a target_department"""
#     target_cols = [col for col in df.columns if target_department in col]
#     df[f"Total {target_department}"] = df[target_cols].sum(axis=1)
#     return df

from enum import Enum


class DepartmentBonus(Enum):
    FINANCE = 1.1
    HR = 1.25
    SALES = 1.1
    RESEARCH = 1.5
    DATA_ANALYTICS = 1.1
    ENGINEERING = 1.3
    MARKETING = 1.4


def bonus_multiplier(
    df: pd.DataFrame,
    target_department: Departments,
) -> pd.DataFrame:
    """Multiplies value by their department bonus rate"""
    target_cols = [col for col in df.columns if target_department in col]
    df[f"Total {target_department}"] = df[target_cols].sum(axis=1)
    return df


df = create_total_spend_column(df, Departments.HR.value)

df
# %%
# ============================== Write up
"""
Here we have a function that sums costs for particular domain-specific aspects of a business, allowing a user to 
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

# %%
