import threading
from collections import Counter
from datetime import datetime
from time import sleep
from yahoo_fin import stock_info as si

import alpaca_trade_api as tradeapi
import yfinance as yf

import KEYS

global api
api = tradeapi.REST(KEYS.TRADE_KEY_ID, KEYS.TRADE_API_SECRET_KEY, base_url="https://paper-api.alpaca.markets")
global net_money

available = []  # stocks to look at
purchased = {}  # stocks bought and how much is bought


def buy(ticker: str, quantity: int):
    api.submit_order(symbol=ticker, qty=quantity, side='buy', type='market', time_in_force='day')


def sell(ticker: str, quantity: int):
    api.submit_order(symbol=ticker, qty=quantity, side='sell', type='market', time_in_force='day')


def query_price(ticker: str):
    print(si.get_live_price(ticker))


