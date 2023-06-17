from typing import Optional
from typing import Union
from dataclasses import dataclass
from datetime import datetime


@dataclass
class CohortOneClient:
    client_id: str
    client_name: str
    client_type: str
    multiplier_rate: str


@dataclass
class CohortTwoClient:
    client_id: str
    client_name: str
    client_type: str
    start_date: datetime
    number_of_employees: int


def calculate_type_one_rate():
    return 1


def calculate_type_two_rate():
    return 2


def get_client():
    return 3


def calculate_rate(client_type: str) -> Union[CohortOneClient, CohortTwoClient]:
    if client_type == "CohortOne":
        return calculate_type_one_rate()
    elif client_type == "CohortTwo":
        return calculate_type_two_rate()
    raise RuntimeError(
        "Should never reach this code," "as an invalid input has been entered"
    )


"""
Suppose you had code that called the calculate_rate function but was only expecting a 
CohortTwoClient type to be returned:
"""


def generate_quote() -> CohortTwoClient:
    client = get_client()
    result = calculate_rate(client.client_type)
    return result


""" The type checker would return:
union_type.py:56: 
error: Incompatible return value type 
    (got "Union[CohortOneClient, CohortTwoClient]", expected "Optional[CohortTwoClient]")  
[return-value]

"""

"""
The fact that the typechecker errors out in this case is fantastic. If any function 
you depend on changes to return a new type, its return signature must be updated to 
Union a new type, which forces you to update your code to handle the new type. This 
means that your code will be flagged when your dependencies change in a way that 
contradicts your assumptions. With the decisions you make today, you can catch errors 
in the future. This is the mark of robust code; you are making it increasingly harder 
for developers to make mistakes, which reduces their error rates, which reduces the 
number of bugs users will experience.
"""


class ClientTypeError(Exception):
    """
    Raised when incorrect usage of a client type is encountered
    """


def generate_quote() -> CohortTwoClient:
    client = get_client()
    if client.client_type == "CohortOne":
        raise ClientTypeError("Quotes should only be generated for CohortTwo clients.")
    client.rate = calculate_rate(client.client_type)
    return client
