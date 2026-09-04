import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

st.title("Explore the insights here")

#DATASET PREVIEW
df = sns.load_dataset('car_crashes')
st.subheader("Dataset Information")

st.write("Shape of Dataset:", df.shape)

st.write("Columns in Dataset:")
st.write(df.columns)

st.write("Dataset Information:")
df.info()

st.write("Statistical Summary:")
st.write(df.describe())

st.dataframe(df)

#FILTERS CONNECTIVITY
df['State'] = df["abbrev"]

#Sidebar
st.sidebar.title("Dashboard Filters")
selected_state = st.sidebar.multiselect(
    "Selected State",
    options = df ["State"],
    default = df ["State"]
)
df['State'] = df["abbrev"]
filtered_df = df[df['State'].isin(selected_state)]

#KPI Cards
col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Accidents %",
    round(filtered_df['total'].mean()),'%'
)

col2.metric(
    "Average Speeding %",
    round(filtered_df['speeding'].mean()),'%'
)

col3.metric(
    "Average alcoholic %",
    round(filtered_df['alcohol'].mean()),'%'
)
#GRAPHS CONNECTIVITY
fig = px.bar(filtered_df,x = 'abbrev',y = 'total',
             title = 'statwise total accidents',
             labels = {'abbrev':'state','total':'total accidents'},
             color = 'total',template = 'plotly_dark')
st.plotly_chart (fig)

fig = px.pie(filtered_df, values = 'speeding', names = 'abbrev',
             title = 'Speeding Accidents Percentage',
             template = 'plotly_dark',
             color_discrete_sequence = px.colors.sequential.algae_r,
             height = 600,width = 600)
fig.update_traces(textposition = 'inside')
st.plotly_chart (fig)

fig = px.scatter(filtered_df,x ='speeding',y = 'alcohol',color = 'total',size = 'total',
                 template = 'plotly_dark')
st.plotly_chart (fig)