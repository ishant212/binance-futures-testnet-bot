import argparse

from bot.client import get_client
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        if order_type == "LIMIT" and not args.price:
            raise ValueError("Price is required for LIMIT orders")

        price = float(args.price) if args.price else None

        print("\n=== ORDER REQUEST SUMMARY ===")
        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Order Type  : {order_type}")
        print(f"Quantity    : {quantity}")

        if price:
            print(f"Price       : {price}")

        client = get_client()

        response = place_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        print("\n=== ORDER RESPONSE ===")
        if response:
            print(response)
        else:
            print("Order submitted successfully to Binance Futures Testnet")

    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()