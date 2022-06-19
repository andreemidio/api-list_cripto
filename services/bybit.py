from utils.connector import http


def get_cripto_values():
    return http.get('https://api-testnet.bybit.com/v2/public/tickers').json()
