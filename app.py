import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
from PIL import Image

import folder1

df=pd.read_csv('My Uber Drives - 2016.csv')
image = Image.open('img.png')

st.sidebar.image('img.png')

st.sidebar.title("UBER ANALYSIS")


user=st.sidebar.radio(
    'select an option',
    ('overall_analysis','trip vs Month','Time vs Trip','Purpose_analysis')
)

if user=='overall_analysis':
    st.title('Overall_analysis')
    new_df=folder1.clean(df)
    st.dataframe(new_df)

if user=='trip vs Month':
    st.title('month have max_trips')

    new_df=folder1.month(df)
    fig = px.bar(new_df, x='month', y='trip')
    st.plotly_chart(fig)

if user=='Time vs Trip':
    x=folder1.time(df)
    fig = px.bar(x, y='trip', x='Hours', text_auto='.2s',
                 title="number of trip vs Hours")
    st.plotly_chart(fig)

if user=='Purpose_analysis':
    y=folder1.purpose(df)
    fig = px.pie(y, values='counts', names='purpose', title='Cabs for purpose')
    st.plotly_chart(fig)





