import argparse
import logging
from src.converter import convert_currency
from src.logger import setup_logger


def main():
    logger = setup_logger()

    parser = argparse.ArgumentParser(
        description="Currency Converter"
    )

    parser.add_argument(
        "--from",
        dest="from_currency",
        required=True,
        help="Currency to convert from (e.g. USD)"
    )

    parser.add_argument(
        "--to",
        dest="to_currency",
        required=True,
        help="Currency to convert to (e.g. INR)"
    )

    parser.add_argument(
        "--amount",
        required=True,
        help="Amount to convert"
    )

    args = parser.parse_args()

    try:
        amount = float(args.amount)

        logger.info(
            f"Conversion requested: {amount} "
            f"{args.from_currency.upper()} to {args.to_currency.upper()}"
        )

        result = convert_currency(
            args.from_currency,
            args.to_currency,
            amount
        )

        print(
            f"{amount:.2f} {args.from_currency.upper()} = "
            f"{result:.2f} {args.to_currency.upper()}"
        )

        logger.info(f"Conversion successful: {result}")

    except ValueError as error:
        print(f"Error: {error}")
        logger.error(str(error))

    except FileNotFoundError:
        print("Error: rates.json file was not found.")
        logger.error("rates.json file was not found.")

    except Exception as error:
        print("Error: Something went wrong. Please try again.")
        logger.error(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()