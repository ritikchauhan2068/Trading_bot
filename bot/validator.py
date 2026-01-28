from loguru import logger
logger.add('bot.log', rotation="1MB")

def validate_symbol(symbol):
    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must end with USDT")

def validate_quantity(quantity):
    if float(quantity) <= 0:
        raise ValueError("Quantity must be greater than zero")

def validate_price(price):
    if float(price) <= 0:
        raise ValueError("Price must be greater than zero")

def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")