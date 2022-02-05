# test
"""
1. 
2. radiobutton con 2 dataset disponibili, ETHUSD e EOSBTC
3. funzione che legge la risposta del radiobutton e a seconda di quello lancia un data_loader(): 

"""

import streamlit as st
import pandas as pd

description = """
Using the HP filter to compose a strategy and test it.
Optimization of the opening signal.
Optimization of TP & SL
"""
st.write(description)
aviables_tickers = ('EOS-BTC','ETH-USDT')

st.radio(label='aviables_tickers', options=aviables_tickers, index=0, format_func=special_internal_function, 
         key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)
