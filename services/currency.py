from currency_converter import CurrencyConverter


def get_conversion_rate(from_currency: str, to_currency: str) -> float:
    converter = CurrencyConverter()
    conversion_rate = converter.convert(amount=1, currency=from_currency, new_currency=to_currency)
    if conversion_rate:
        return conversion_rate
