import sys
from bot.client import client
from bot.validator import validate_symbol, validate_quantity,validate_price,validate_side
from loguru import logger

def place_market_order(client, symbol, side, quantity):
    validate_symbol(symbol)
    validate_quantity(quantity)
    validate_side(side)

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

    logger.info(f"Market order placed: {order}")
    return order


def place_limit_order(client, symbol, side, quantity, price):
    validate_symbol(symbol)
    validate_quantity(quantity)
    validate_price(price)
    validate_side(side)

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )

    logger.info(f"Limit order placed: {order}")
    return order