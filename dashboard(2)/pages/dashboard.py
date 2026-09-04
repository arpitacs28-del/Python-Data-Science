import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

st.title("Explore the insights here")

#DATASET PREVIEW
df = sns.load_dataset('titanic')
st.dataframe(df)

#FILTERS CONNECTIVITY


#Sidebar
st.sidebar.title("Dashboard Filters")
selected_gender = st.sidebar.multiselect(
    "selected_gender",
    options = df ["sex"].unique(),
    default = df ["sex"].unique()
)

filtered_df = df[df["sex"].isin(selected_gender)]

# KPI Cards
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Passengers",
    len(filtered_df)
)

col2.metric(
    "Survivors",
    filtered_df['survived'].sum()
)

col3.metric(
    "Deaths",
    (filtered_df['survived'] == 0).sum()
)
#GRAPHS CONNECTIVITY

fig = px.bar(filtered_df,x = 'class',y = 'fare',
             title = 'classwise total fare',
             labels = {'class':'class','fare':' total fare'},
             color = 'fare',template = 'plotly_dark')
st.plotly_chart (fig)

fig = px.pie(filtered_df, values = 'survived', names = 'who',
             title = 'survived vs who',
             template = 'plotly_dark',
             color_discrete_sequence = px.colors.sequential.Blues_r,
             height = 600,width = 600)
fig.update_traces(textposition = 'inside')
st.plotly_chart (fig)

fig = px.bar(filtered_df,x = 'survived',y = 'who',
             title = 'total survived vs who',
             labels = {'class':'survived','fare':' total who'},
             color = 'fare',template = 'plotly_dark')
st.plotly_chart (fig)

