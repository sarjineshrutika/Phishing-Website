import streamlit as st
import pandas as pd
import numpy as np

st.write("djsg")

df = pd.DataFrame({
  'first column': ['a', 'b', 'c', 'd'],
  'second column': [10, 20, 30, 40]
})

st.write(df)
st.table(df)

st.line_chart(df['second column'])

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [ 19.07283000 ,72.88261000  ],
    columns=['lat', 'lon'])

st.map(map_data)

st.slider('x')

st.button('x')

st.selectbox(options=['dghjf','d'],label='d')

st.text_input("Your name",key="name")
st.number_input("df")

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)
