# test
"""
DONE
 radiobutton con 2 dataset disponibili, ETHUSD e EOSBTC
funzione che legge la risposta del radiobutton e a seconda di quello lancia un data_loader(): 

TO DO 
applica le bollinger bands alla decomposizione, le bollinger hanno una finestra per essere calcolate
prova ad entrare al rialzo quando sta sotto < % di probabilita' della bollinger bands


optimization of the opening signal
optimization of TP & SL
"""
import streamlit as st

import pandas as pd
import statsmodels.api as sm

description = """
Hodrick–Prescott filter Trading Strategy based Backtester 
Seasonality decomposition in time series analysis with Hodrick–Prescott filter
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

def app():
    if  'EOS' in choosen_ticker:
        st.write('EOS-BTC incoming')
        df = pd.read_csv('eos-usd.csv')
        st.write(df.head())
        st.line_chart(df['price'])
        # PRICE DECOMPOSITION
        data_cycle, data_trend = sm.tsa.filters.hpfilter(df['price'])
        st.line_chart(data_cycle)
        st.line_chart(data_trend)

        # VOLUME DECOMPOSITION
        data_cycle_vol, data_trend_vol = sm.tsa.filters.hpfilter(df['total_volume'])
        st.line_chart(data_cycle_vol)
        st.line_chart(data_trend_vol)

    elif 'ETH' in choosen_ticker:
        st.write("ETH-USD incoming")
        df = pd.read_csv('eth-usd-2021-1m.csv')
        st.write(df.head())
        st.line_chart(df['close'])

    else:
        st.write("Sorry, we could't solve your request")


app()

# 
# plt.figure(figsize=(25,20))
# plt.plot(data_cycle)

# 
# 