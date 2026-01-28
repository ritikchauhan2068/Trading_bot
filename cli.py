from bot.client import client
from bot.orders import place_market_order,place_limit_order
import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("symbol")
    parser.add_argument("side", choices=["BUY", "SELL"])
    parser.add_argument("type", choices=["MARKET", "LIMIT"])
    parser.add_argument("qty", type=float)
    parser.add_argument("price", nargs="?")
    args = parser.parse_args()

    if args.type == "MARKET":
        order = place_market_order(
            client, args.symbol, args.side, args.qty
        )
    else:
        if args.price is None:
            raise ValueError("Price required for LIMIT order")

        order = place_limit_order(
            client, args.symbol, args.side, args.qty, args.price
        )

    print("✅ Order placed successfully")
    print(order)

if __name__ == "__main__":
    main()