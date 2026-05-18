from bot.logging_config import logger
from binance.exceptions import BinanceAPIException


def place_order(client, symbol, side, order_type, quantity, price=None):

    try:

        params = {
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "newOrderRespType": "RESULT"
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"Order Request: {params}")

        response = client.futures_create_order(**params)

        logger.info(f"Order Response: {response}")

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise