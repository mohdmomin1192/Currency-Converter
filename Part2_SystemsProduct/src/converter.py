import json
import os


def load_rates():
    """Load exchange rates from rates.json."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    rates_file = os.path.join(base_dir, "rates.json")

    with open(rates_file, "r") as file:
        return json.load(file)


def convert_currency(from_currency, to_currency, amount):
    """Convert an amount from one currency to another."""

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a valid number.")

    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    rates = load_rates()

    if from_currency not in rates:
        raise ValueError(f"Unsupported currency code: {from_currency}")

    if to_currency not in rates:
        raise ValueError(f"Unsupported currency code: {to_currency}")

    # Rates are relative to USD
    amount_in_usd = amount / rates[from_currency]
    converted_amount = amount_in_usd * rates[to_currency]

    return converted_amount