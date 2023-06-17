# %%
import pandas as pd
from typing import Optional

map = {"one": "microsoft", "two": "apple"}

df = pd.DataFrame({"emp_code": ["aa", "bb"], "cohort": ["one", "two"]})


def map_cohorts_to_brands(
    df: pd.DataFrame,
    cohort_brand_map: dict,
):
    """Maps internal cohort names to a client-facing Brand name"""
    df["brand"] = df["cohort"].map(cohort_brand_map)
    return df


"""
By explicitly specifying Optional, you encourage safer coding practices by encouraging 
developers to handle the case where a value is None and preventing potential None-related errors such as attribute access on a None object.
"""


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


"""
alternatively, "brand" might have a default
"""


def map_cohorts_to_brands_v2(
    df: pd.DataFrame,
    cohort_brand_map: Optional[dict],
):
    """Maps internal cohort names to a client-facing Brand name"""
    if cohort_brand_map is None:
        df["brand"] = "NonBrandedCohort"
    else:
        df["brand"] = df["cohort"].map(cohort_brand_map)
    return df


df = map_cohorts_to_brands_v2(df, map)
"""
Either way, you are communicating to future engineers that None should be expected, and 
any updates should handle the None case.
"""

# %% More from ChatGPT:
"""
The `Optional` type, also known as Union with `None`, is commonly used in Python type annotations to indicate that a variable or function parameter can accept either a specific type or `None`. It brings several benefits to the codebase:

1. Enhanced clarity: By using `Optional`, you explicitly communicate to both humans and static analysis tools that a value can be of a certain type or `None`. This improves code readability and reduces ambiguity.

2. Expressive intent: Type annotations serve as documentation, and using `Optional` conveys your intention that a particular argument or variable is allowed to be nullable. This helps other developers understand how the code is expected to behave.

3. Type checking support: Static type checkers like `mypy` can leverage the information provided by `Optional` annotations to detect potential errors and bugs at compile-time. These tools can catch cases where you're inadvertently passing `None` or not handling nullable values correctly.

4. Safer coding practices: By explicitly specifying `Optional`, you encourage safer coding practices by encouraging developers to handle the case where a value is `None` and preventing potential `None`-related errors such as attribute access on a `None` object.

5. Improved API design: By using `Optional` in function signatures, you make it clear to callers that certain arguments are optional. This promotes better API design and reduces the need for comments or extra documentation to explain the expected behavior.

6. Avoiding runtime errors: By catching nullable-related errors during development through static type checking, you can reduce the likelihood of encountering such errors at runtime. This leads to more robust and reliable code.

Overall, the use of `Optional` type annotations in Python helps in making your code more explicit, readable, and safer, while also providing benefits during development and maintenance through improved type checking support."""
