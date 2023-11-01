""" 
To determine the quotation of one currency to another, we would divide 
the exchange rate of the origin currency by the exchange rate of the 
target currency. This will give us the rate at which one unit of the origin
 currency is exchanged for the target currency.

Here's how you can implement the quotation method:
"""


import decimal
import typing

from app.currency import Currency
from app.rates import RATES


class ExchangeRateService:
    _rates = RATES

    def update_rate(self, currency: Currency, rate: decimal.Decimal):
        self._rates[currency] = rate

    def get_rate(self, currency: Currency) -> typing.Optional[decimal.Decimal]:
        try:
            return self._rates[currency]
        except KeyError:
            return None

    def quotation(
        self, origin: Currency, target: Currency
    ) -> typing.Optional[decimal.Decimal]:
        """TODO: Part 2"""

    def quotation(
        self, origin: Currency, target: Currency
    ) -> typing.Optional[decimal.Decimal]:
        """Returns the exchange rate for the supplied currency pair."""
        origin_rate = self.get_rate(origin)
        target_rate = self.get_rate(target)

        # Ensure both rates are present and are not zero
        if not origin_rate or not target_rate or target_rate == decimal.Decimal("0"):
            raise QuotationError(
                f"Invalid rate for {origin.name}/{target.name} currency pair"
            )

        # Return exchange rate by dividing original rate by target rate
        return decimal.Decimal(origin_rate) / decimal.Decimal(target_rate)


exchange_rate_service = ExchangeRateService()
