import streamlit as st
import pandas as pd

data={
  'series_1':[1,3,4,5,7],
  'series_2':[10,30,40,100,250]
}

df=pandas.DataFrame(data)

st.title('My First Streamlit App')
st.subheader('Introduction Streamlit in Automate Everything with Python')
st.write('''This is my first web app enjoy it''')
st.write(df)
st.line_chart(df)