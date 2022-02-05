# test
"""
DONE
 radiobutton con 2 dataset disponibili, ETHUSD e EOSBTC

TO DO 
funzione che legge la risposta del radiobutton e a seconda di quello lancia un data_loader(): 


optimization of the opening signal
optimization of TP & SL
"""

import streamlit as st
import pandas as pd

description = """
Using the HP filter to compose a strategy and test it. \n
"""
st.write(description)
aviables_tickers = ('EOS-USD | 2017 -> Feb 2022 1 day ','ETH-USD | 1 Jan 2020 -> 1 Jan 2021 1 minute ')


choosen_ticker = st.radio(label='Aviables Tickers ', options=aviables_tickers)



def load_dataset():
    if  'EOS' in choosen_ticker:
        st.write('EOS-BTC incoming')
        df = pd.read_csv('eos-usd.csv')
        st.write(df.head())
    elif 'ETH' in choosen_ticker:
        st.write("ETH-USD incoming")
        df = pd.read_csv('eth-usd-2021-1m.csv')
        st.write(df.head())

    else:
        st.write("Sorry, we could't solve your request")

load_dataset()