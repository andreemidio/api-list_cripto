import logging

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from services.list_tickers import list_five_tickers
from respository.tickers import Tickers
from services.bybit import get_cripto_values

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    logging.info("Application is up")


@app.on_event("shutdown")
def shutdown_event():
    logging.error("Application is down")


@app.get("/tickers")
async def get_tickers() -> Tickers:
    data = get_cripto_values()

    values = list_five_tickers(data=data)

    return values


@app.get("/tickers/{id}")
async def get_tickers(id: int) -> Tickers:
    data = get_cripto_values()

    values = list_five_tickers(data=data)

    return values[id]


@app.post("/tickers")
async def create_tickers(tickers: Tickers) -> Tickers:
    return tickers


@app.put("/tickers/{id}")
async def update_tickers(id: int, tickers: Tickers) -> Tickers:
    data = get_cripto_values()

    values = list_five_tickers(data=data)

    stored_item_data = values[id]
    stored_item_model = Tickers(**stored_item_data)
    update_data = tickers.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    values[id] = jsonable_encoder(updated_item)

    return updated_item


@app.delete("/tickers/{id}")
async def delete_tickers(id: int, tickers: Tickers) -> Tickers:
    data = get_cripto_values()

    values = list_five_tickers(data=data)

    ticker_to_remove = values[id]

    if ticker_to_remove is not None:
        values.remove(ticker_to_remove)

    return {"info": "ticker removed"}
