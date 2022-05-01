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
Seasonality decomposition in time series analysis with Hodrick–Prescott filter
\n
The Hodrick–Prescott filter is a mathematical tool used in macroeconomics, 
especially in real business cycle theory, to remove the cyclical component 
of a time series from raw data. It is used to obtain a smoothed-curve representation
of a time series, one that is more sensitive to long-term than to short-term fluctuations.
\n
"""

st.write(description)

datasets_available  = ("Microsoft MSFT - adjusted close price - daily - 2017-01-03 to 2021-09-10",
                       "(Test) Apple APPL")

choosen_ticker = st.radio(label='Datesets avaiable:', options=datasets_available)

def app():
    if  'Microsoft' in choosen_ticker:
        
        df = pd.read_csv('MSFT.csv')
        
        st.write('Microsoft (MSFT) dataset (first 5 rows)')
        st.write(df.head())
        
        st.write('Microsoft daily adjusted close price ')
        st.line_chart(df['Adj Close'])

        # PRICE DECOMPOSITION
        data_cycle, data_trend = sm.tsa.filters.hpfilter(df['Adj Close'])
        
        st.write("Mircosoft data")
        st.area_chart(data_cycle)
        
        st.write("Microsoft data trend with HP filter")
        st.line_chart(data_trend)
        
        st.write("Microsoft daily return")
        st.area_chart(df['daily_return'])

    else:
        st.write("Sorry, we could't solve your request")

app()