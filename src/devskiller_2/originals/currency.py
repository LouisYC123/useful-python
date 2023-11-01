from enum import Enum


class Currency(Enum):
    PLN = "PLN"
    CZK = "CZK"
    DKK = "DKK"
    EUR = "EUR"
    GBP = "GBP"
    NOK = "NOK"
    USD = "USD"
    ZAR = "ZAR"

    @classmethod
    def is_member(cls, value: str) -> bool:
        """TODO: Part 1"""
