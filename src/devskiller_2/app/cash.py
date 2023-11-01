""" 
To implement the `Cash.to()` method, we'll first check if the target_currency
is the same as the Cash instance's currency. If they're the same, we can simply
return the instance. If they're different, we'll calculate the new amount based 
on the exchange rate from the ExchangeRateService.

Next, to allow for the use of the @ operator for currency conversion, we'll
implement the __matmul__ special method, which is invoked when the @ operator is used.

Here's the code:
"""

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

    """ 
    Here's the modified __add__ method after implementing the context manager
    """

    def __add__(self, other: CashOrNumber) -> "Cash":
        amount = self.amount + self._get_amount(other)
        result_currency = TargetCurrency.get_target_currency() or self.currency
        if result_currency != self.currency:
            return Cash(amount, self.currency).to(result_currency)
        return Cash(amount, result_currency)

    """ 
    Like with __add__, this method first calculates the new amount, then 
    checks if a target currency is set in the context using TargetCurrency.get_target_currency().
     If a target currency is active and different from the current currency, it converts the 
     result into that currency. Otherwise, it returns the result in the current currency.
    """

    def __sub__(self, other: CashOrNumber) -> "Cash":
        other_amount = self._get_amount(other)
        result_amount = self.amount - other_amount

        return Cash(str(result_amount), self.currency)

    def __radd__(self, other: CashOrNumber) -> "Cash":
        return self.__add__(other)

    def __neg__(self) -> "Cash":
        return Cash(-self._amount, self.currency)

    def __pos__(self) -> "Cash":
        return Cash(+self._amount, self.currency)

    def __abs__(self) -> "Cash":
        return Cash(abs(self._amount), self.currency)

    """ 
    Implementing the @ operator for currency conversion:
    """

    def __matmul__(self, target_currency: Currency) -> "Cash":
        return self.to(target_currency)

    def to(self, target_currency: Currency) -> "Cash":
        if target_currency is None or target_currency == self.currency:
            return self

        rate = exchange_rate_service.quotation(self.currency, target_currency)
        if rate is None:
            raise ExchangeRateUnknownError(
                f"Exchange rate for {self.currency.name} to {target_currency.name} is unknown."
            )

        new_amount = self.amount * rate

        return Cash(new_amount, target_currency)

    def _get_amount(self, other: CashOrNumber) -> decimal.Decimal:
        if isinstance(other, Cash):
            other_converted = other.to(self.currency)
            return other_converted.amount
        elif isinstance(other, (int, decimal.Decimal)):
            return decimal.Decimal(other)
        else:
            raise ValueError(f"Unsupported operand type: {type(other)}")


""" 
o create a context manager, the TargetCurrency class needs to 
define the __enter__ and __exit__ methods. 

To make the Cash class operations respect the target currency set by
 the TargetCurrency context manager, you need to modify the operations in the Cash class.

For example, in the __add__ method, instead of just returning Cash(amount, self.currency), 
you should check if there's a target currency set, and if so, convert the result 
to that currency.

We can utilize a class variable in TargetCurrency to store the target
currency and leverage the __enter__ and __exit__ methods of the context manager to 
manage its value.

This implementation would store the _target_currency in memory for the entire process, 
and the context manager would change its value. This approach will work fine for 
single-threaded applications. However, if you are planning to use this code in a 
multi-threaded application, different threads will overwrite each other's target currency, 
causing unpredictable behavior. That's why using threading.local is recommended for
multi-threaded applications.

"""


class TargetCurrency:
    _target_currency = None

    def __init__(self, target_currency: Currency):
        self.previous_currency = None
        self.new_currency = target_currency

    def __enter__(self):
        if TargetCurrency._target_currency:
            self.previous_currency = TargetCurrency._target_currency
        TargetCurrency._target_currency = self.new_currency

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Restore the original target currency or set it to None if there wasn't any
        TargetCurrency._target_currency = self.previous_currency

    @classmethod
    def get_target_currency(cls) -> Currency:
        return cls._target_currency
