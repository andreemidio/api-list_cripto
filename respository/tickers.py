from pydantic import BaseModel, validator
import pendulum


class Tickers(BaseModel):
    id: int
    symbol: str
    last_price: str
    next_funding_time: str

    @validator("next_funding_time", pre=True)
    def parse_birthdate(cls, value):
        date_value = pendulum.parse(value)

        return date_value.format("DD/M/Y")
