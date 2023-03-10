import streamlit as st
import altair as alt
from pandas_datareader import data as pdr
from datetime import datetime, timedelta
import yfinance as yf
from streamlit_extras.let_it_rain import rain
import pandas as pd
import numpy as np




# config
st.set_page_config(layout="wide", page_title="Hello", page_icon="๐ ")

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


# ์๋จ๋ฐ ์จ๊ธฐ๊ธฐ
hide_decoration_bar_style = '''
    <style>
        header {height: 10.125rem;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

@st.cache(allow_output_mutation=True)
def Pageviews():
    return []

pageviews=Pageviews()
pageviews.append('dummy')


try:
    st.markdown('๋ฐฉ๋ฌธ์ ์ : {}'.format(len(pageviews)))
except ValueError:
    st.markdown('๋ฐฉ๋ฌธ์ ์ : {}'.format(1))


# rain
rain(
    emoji="๐",
    font_size=10,
    falling_speed=22,
    animation_length="infinite",
)


yf.pdr_override()



dict = {'์ผ์ฑ์ ์':'005930.KS', 'ํํ์์คํ':'272210.KS', '๋์ฐ์กฐ์ ํด์': '042660.KS'}


option = st.sidebar.selectbox(
'์ข๋ชฉ๋ช',
(dict.keys()))


sevendayago = datetime.today() - timedelta(17)

start_date = st.sidebar.date_input('์์์ผ', sevendayago)
end_date = st.sidebar.date_input('์ข๋ฃ์ผ', datetime.today())

print(start_date)


st.title(f'๐ {option} ์ฃผ๊ฐ')

st.write('''
๋ง๊ฐ ๊ฐ๊ฒฉ๊ณผ ๊ฑฐ๋๋์ ์ฐจํธ๋ก ๋ณด์ฌ์ค๋๋ค!
''')

st.markdown("----", unsafe_allow_html=True)


# https://finance.yahoo.com/quote/005930.KS?p=005930.KS
dr = pdr.get_data_yahoo(dict[option], start_date, end_date)

dr.reset_index(inplace=True)

dr['Date'] = pd.to_datetime(dr['Date']).dt.date
st.dataframe( dr)






# chart_data = alt.Chart(dr).mark_line(    
#     point={
#       "filled": True,
#       "fill": "red"
#     }).encode(
#     alt.X('Date', title='๋ ์ง', axis=alt.Axis(tickCount="day")),
#     alt.Y(['Close','Open'], title='๊ฐ๊ฒฉ'),
#     tooltip='Close',
# )


chart_data = alt.Chart(dr).transform_fold(
    ['Open', 'Close'],
    as_=['Type', 'price']
).mark_line(
        point={
       "filled": True,
       "fill": "red"
     }).encode(
     alt.X('Date:T', title='๋ ์ง', axis=alt.Axis(tickCount="day")),
     alt.Y('price:Q', title='๊ฐ๊ฒฉ'),
    color='Type:N'
)



nearest = alt.selection(type='single', nearest=True, on='mouseover',
                        fields=['x'], empty='none')

st.write('''๋ง๊ฐ ๊ฐ๊ฒฉ''')
st.altair_chart(chart_data, use_container_width=True)





# st.write('''๋ง๊ฐ ๊ฐ๊ฒฉ''')
# st.line_chart(dr.Close)

# st.write('''๊ฑฐ๋๋''')
# st.line_chart(dr.Volume)
