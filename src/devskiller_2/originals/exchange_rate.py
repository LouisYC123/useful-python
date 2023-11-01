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


exchange_rate_service = ExchangeRateService()
