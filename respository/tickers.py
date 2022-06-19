from typing import Optional

import pendulum
from pydantic import BaseModel, validator


class Tickers(BaseModel):
    id: Optional[int]
    symbol: str
    last_price: str
    next_funding_time: str

    @validator("symbol", pre=True)
    def parse_symbol(cls, value):
        return value[0:3]

    @validator("next_funding_time", pre=True)
    def parse_birthdate(cls, value):
        if value is None or value == '':
            return pendulum.now().format("DD/M/Y")

        date_value = pendulum.parse(value)

        return date_value.format("DD/M/Y")
