# %%
import pandas as pd
from typing import Optional

map = {"one": "microsoft", "two": "apple"}
map = None
df = pd.DataFrame({"emp_code": ["aa", "bb"], "cohort": ["one", "two"]})


def map_cohorts_to_brands(
    df: pd.DataFrame,
    cohort_brand_map: dict,
):
    """Maps internal cohort names to a client-facing Brand name"""
    df["brand"] = df["cohort"].map(cohort_brand_map)
    return df


def map_cohorts_to_brands_v2(
    df: pd.DataFrame,
    cohort_brand_map: Optional[dict],
):
    """Maps internal cohort names to a client-facing Brand name"""
    if cohort_brand_map is None:
        raise AttributeError(
            "cohort_brand_map has not been set, please revisit section one"
        )
    else:
        df["brand"] = df["cohort"].map(cohort_brand_map)
        return df


df = map_cohorts_to_brands_v2(df, map)

# %%
