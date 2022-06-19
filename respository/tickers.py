from typing import Iterable
from pydantic import BaseModel


class Tickers(BaseModel):
    id: int
    symbol: str
    last_price: str
    next_funding_time: str
