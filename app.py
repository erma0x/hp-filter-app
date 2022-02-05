# test
"""
1. 
2. radiobutton con 2 dataset disponibili, ETHUSD e EOSBTC
3. funzione che legge la risposta del radiobutton e a seconda di quello lancia un data_loader(): 

"""

import streamlit as st
import pandas as pd

description = """
Using the HP filter to compose a strategy and test it. \n
Optimization of the opening signal. \n
Optimization of TP & SL \n
"""
st.write(description)
aviables_tickers = ('EOS-BTC','ETH-USDT')

st.radio(label='aviables tickers', options=aviables_tickers)
