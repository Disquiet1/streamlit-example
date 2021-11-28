import streamlit as st
import pandas as pd
import yfinance as yf

st.write("""Chain Link Price""")

tickerSymbol = 'LINK-USD'

tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2019-1-1', end='2021-1-1')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
