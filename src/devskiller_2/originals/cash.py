import decimal

import typing

from app.currency import Currency
from app.exchange_rate import exchange_rate_service
from app.exceptions import ExchangeRateUnknownError, InvalidCurrencyError

CashOrNumber = typing.Union[int, decimal.Decimal, "Cash"]


class Cash:
    __slots__ = "_amount", "_currency"

    def __init__(
        self, amount: typing.Union[str, decimal.Decimal], currency: Currency
    ) -> None:
        if not isinstance(currency, Currency) or not Currency.is_member(currency.value):
            raise InvalidCurrencyError

        self._amount = decimal.Decimal(amount)
        self._currency = currency

    @property
    def amount(self) -> decimal.Decimal:
        return self._amount.quantize(decimal.Decimal("0.0000"))

    @property
    def currency(self) -> Currency:
        return self._currency

    def __repr__(self) -> str:
        return f"{self.amount} {self.currency.name}"

    def __lt__(self, other: CashOrNumber) -> bool:
        amount = self._get_amount(other)
        return self.amount < amount

    def __le__(self, other: CashOrNumber) -> bool:
        amount = self._get_amount(other)
        return self.amount <= amount

    def __gt__(self, other: CashOrNumber) -> bool:
        amount = self._get_amount(other)
        return self.amount > amount

    def __ge__(self, other: CashOrNumber) -> bool:
        amount = self._get_amount(other)
        return self.amount >= amount

    def __eq__(self, other: CashOrNumber) -> bool:
        amount = self._get_amount(other)
        return self.amount == amount

    def __ne__(self, other: CashOrNumber) -> bool:
        return not self == other

    def __bool__(self):
        return bool(self._amount)

    def __add__(self, other: CashOrNumber) -> "Cash":
        amount = self.amount + self._get_amount(other)

        return Cash(amount, self.currency)

    def __radd__(self, other: CashOrNumber) -> "Cash":
        return self.__add__(other)

    def __neg__(self) -> "Cash":
        return Cash(-self._amount, self.currency)

    def __pos__(self) -> "Cash":
        return Cash(+self._amount, self.currency)

    def __abs__(self) -> "Cash":
        return Cash(abs(self._amount), self.currency)

    def to(self, target_currency: Currency) -> "Cash":
        """TODO: Part 3"""

    def _get_amount(self, other: CashOrNumber) -> decimal.Decimal:
        if isinstance(other, Cash):
            other = other.to(self.currency)
            return other.amount
        return other


class TargetCurrency:
    """TODO: Part 4"""

    def __init__(self, *args, **kwargs):
        pass
