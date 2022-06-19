import json
from operator import itemgetter

from respository.tickers import Tickers


def list_five_tickers(data: dict):
    values = data["result"]

    newlist = sorted(values, key=lambda x: x['last_price'], reverse=True)[0:5]
    tickers = list()
    for i, d in enumerate(newlist):
        tickers.append(Tickers(
            id=i,
            symbol=d["symbol"],
            last_price=d["last_price"],
            next_funding_time=d["next_funding_time"]
        ).dict())

    return tickers
