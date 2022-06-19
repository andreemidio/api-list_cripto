import json
import operator
from operator import itemgetter

from respository.tickers import Tickers
from services.bybit import get_cripto_values


def list_five_tickers():
    data = get_cripto_values()
    values = data["result"]

    newlist = sorted(values, reverse=True, key=lambda x: float(operator.itemgetter("last_price")(x)))[:5]

    tickers = list()
    for i, d in enumerate(newlist):
        tickers.append(Tickers(
            id=i,
            symbol=d["symbol"],
            last_price=d["last_price"],
            next_funding_time=d["next_funding_time"]
        ).dict())

    return tickers


if __name__ == '__main__':
    with open("../tickers.json") as f:
        data = json.load(f)

    print(list_five_tickers(data))
