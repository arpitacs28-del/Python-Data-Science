import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Discover the world of EV's")

#DATASET PREVIEW
df = pd.read_csv('EV_Adoption_and_Range_Anxiety_Dataset.csv')
st.dataframe(df)

#GRAPH CONNECTIVITY
fig = px.bar(df,x = 'Will_Buy_EV',
             title = 'Willingness to buy EV',
            color_discrete_map={
    'Yes': 'green',
    'No': 'red'
},template = 'plotly_dark')

st.plotly_chart (fig)