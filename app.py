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
Time Series Analysis: seasonality decomposition with Hodrick–Prescott filter
\n
The Hodrick–Prescott filter is a mathematical tool used in macroeconomics, 
especially in real business cycle theory, to remove the cyclical component 
of a time series from raw data. It is used to obtain a smoothed-curve representation
of a time series, one that is more sensitive to long-term than to short-term fluctuations.
\n
"""
st.write(description)
datasets_available  = ('EOS-USD | 2017 - Feb 2022 | frequency: 1 day  ',
                        'ETH-USD | 28 Jul 2020 - 1 Jan 2021 | frequency: 1 minute ')

choosen_ticker = st.radio(label='Datesets avaiable:', options=datasets_available)

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

    return(df)

df = load_dataset()

st.line_chart(df['close'])

# data_cycle, data_trend = sm.tsa.filters.hpfilter(df['close'])
# st.line_chart(df['close'])

# df['close'].plot(figsize=(25,20))
# plt.ylabel("ETH vs USD")

# # PRICE DECOMPOSITION
# plt.figure(figsize=(25,20))
# plt.plot(data_cycle)

# # VOLUME DECOMPOSITION
# data_cycle, data_trend = sm.tsa.filters.hpfilter(df['volume'])