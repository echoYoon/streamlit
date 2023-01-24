import streamlit as st
import altair as alt
from pandas_datareader import data as pdr
from datetime import datetime, timedelta
import yfinance as yf
from streamlit_extras.let_it_rain import rain
import pandas as pd
import numpy as np

# config
st.set_page_config(layout="wide", page_title="Hello", page_icon="🏠")

streamlit_style = """
			<style>
@font-face {
    font-family: 'ChosunGu';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@1.0/ChosunGu.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

			html, body, [class*="css"]  {
			font-family: 'ChosunGu', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

# rain
rain(
    emoji="🌟",
    font_size=10,
    falling_speed=22,
    animation_length="infinite",
)


yf.pdr_override()



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

dr.reset_index(inplace=True)

dr['Date'] = pd.to_datetime(dr['Date']).dt.date
st.dataframe( dr)

chart_data = alt.Chart(dr).mark_line(    
    point={
      "filled": True,
      "fill": "red"
    }).encode(
    alt.X('Date', title='날짜', axis=alt.Axis(tickCount="day")),
    alt.Y('Close', title='가격'),
    tooltip='Close',
)

nearest = alt.selection(type='single', nearest=True, on='mouseover',
                        fields=['x'], empty='none')

st.write('''마감 가격''')
st.altair_chart(chart_data, use_container_width=True)





st.write('''마감 가격''')
st.line_chart(dr.Close)

st.write('''거래량''')
st.line_chart(dr.Volume)
