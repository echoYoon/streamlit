import streamlit as st
from pandas_datareader import data as pdr
from datetime import datetime, timedelta
import yfinance as yf

yf.pdr_override()

st.set_page_config(layout="wide", page_title="Hello", page_icon="🏠")

streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Nanum Gothic', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

dict = {'삼성전자':'005930.KS', '한화시스템':'272210.KS', '대우조선해양': '042660.KS'}


option = st.sidebar.selectbox(
'종목명',
(dict.keys()))


sevendayago = datetime.today() - timedelta(7)

start_date = st.sidebar.date_input('시작일', sevendayago)
end_date = st.sidebar.date_input('종료일', datetime.today())

print(start_date)


st.title(f'📈 {option} 주가')

st.write('''
마감 가격과 거래량을 차트로 보여줍니다!
''')

st.markdown("----", unsafe_allow_html=True)


# https://finance.yahoo.com/quote/005930.KS?p=005930.KS
dr = pdr.get_data_yahoo(dict[option], start_date, end_date)

st.write('''마감 가격''')
st.line_chart(dr.Close)

st.write('''거래량''')
st.line_chart(dr.Volume)
