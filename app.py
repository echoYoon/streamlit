import streamlit as st
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
from datetime import datetime, timedelta
import yfinance as yf


streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Nanum Gothic', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

st.sidebar.header('Menu')


sevendayago = datetime.today() - timedelta(7)

start_date = st.sidebar.date_input('시작일', sevendayago)
end_date = st.sidebar.date_input('종료일', datetime.today())


st.title('📈 삼성전자 주가')

st.write('''
마감 가격과 거래량을 차트로 보여줍니다!
''')

st.markdown("----", unsafe_allow_html=True)


yf.pdr_override()

# https://finance.yahoo.com/quote/005930.KS?p=005930.KS
dr = pdr.get_data_yahoo('005930.KS',start_date,end_date)

st.write('''마감 가격''')
st.line_chart(dr.Close)

st.write('''거래량''')
st.line_chart(dr.Volume)
