import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

url = 'https://github.com/esnt/Data/raw/main/Names/popular_names.csv'

df = pd.read_csv(url)

names = list(df['name'].unique())
names.append('All')

st.title('Baby Names')
selected_name = st.text_input('Baby Name','Enter Baby Name')
name_df = df[df['name']==selected_name]


fig = px.scatter(data_frame=name_df,x='year',y='n', color='sex')
fig.update_layout(title=f'Name Trend for {selected_name} from 1910-2021')
st.plotly_chart(fig)
