import_config = get_import_config(config_path)
cohort_id = import_config["cohort"]["cohort_id"]

"""
If you were reviewing the code, how would you know that this code is right? 
If you wanted to also print out the calories, how do you access the data? 
What guarantees do you have about the fields inside of this dictionary? 
To answer these questions, you have two options: 
    - Look up the API documentation (if any) and confirm that the right fields are being used. In this scenario, you
         hope that the documentation is actually complete and correct. 
    - Run the code and print out the returned dictionary. In this situation, 
        you hope that test responses are pretty identical to production responses.

The problem is that you are requiring every reader, reviewer, and maintainer to 
do one of these two steps in order to understand the code. If they don’t, 
you will not get good code review feedback and developers will run the 
risk of using the response incorrectly.

This leads to incorrect assumptions and brittle code. TypedDict allows you to encode what you’ve l
earned about that API directly into your type system.

"""
# TODO - TURN THIS INTO A MORE DE LOOKING API CALL OBJECT
from typing import TypedDict, Literal


class Range(TypedDict):
    min: float
    max: float


class CohortInformation(TypedDict):
    cohort_id: int
    cohort_name: str
    confidence_range_95_percent: Range
    employer_type: int


class PipelineConfig(TypedDict):
    max_employees: int
    cohort: CohortInformation
    data_val_library: Literal["Pandera", "GreatExpectations"]


import_config: PipelineConfig = get_import_config(config_path)

"""
Now it is incredibly apparent exactly what data types you can rely upon. If the API ever changes, a 
developer can update all the TypedDict classes and let the typechecker catch any incongruities. Your 
typechecker now completely understands your dictionary, and readers of your code can reason about 
responses without having to do any external searching. Even better, these TypedDict collections can be as 
arbitrarily complex as you need them to be. You’ll see that I nested TypedDict instances for reusability purposes,
but you can also embed your own custom types, Unions, and Optionals to reflect the possibilities that an API can 
return. And while I’ve mostly been talking about API, remember that these benefits apply to any heterogeneous 
dictionary, such as when reading JSON or YAML.


"""
