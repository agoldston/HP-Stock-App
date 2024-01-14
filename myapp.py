import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Stock Price App

Shown are the stock closing price and volume of Hewlett-Packard!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'HPQ'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2023-1-10')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""## Closing Price by Day
""")
st.line_chart(tickerDf.Close)
st.write(""" ## Trading Volume by Day
""")
st.line_chart(tickerDf.Volume)