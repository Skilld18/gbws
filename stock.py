#!/usr/bin/python

import yfinance as yf

msft = yf.Ticker("AIR.PA")
price = float(msft.info["currentPrice"])
if price > 130:
    print(f"price is {price}")
