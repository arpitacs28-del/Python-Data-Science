import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Discover the world of EV's")

#DATASET PREVIEW
df = pd.read_csv('EV_Adoption_and_Range_Anxiety_Dataset.csv')
st.dataframe(df)

#Sidebars

gender = st.sidebar.multiselect(
    "Select Gender",
    df["Gender"].unique()
)
if gender:
    filtered_df = df[df["Gender"].isin(gender)]
else:
    filtered_df = df

age = st.sidebar.slider(
    "Select Age",
    df["Age"].min(),
    df["Age"].max(),
    value=(df["Age"].min(), df["Age"].max())
)

filtered_df = filtered_df[
    (filtered_df["Age"] >= age[0]) &
    (filtered_df["Age"] <= age[1])
]

city = st.sidebar.multiselect(
    "Select City Type",
    df["City_Type"].unique()
)
if city:
    filtered_df = filtered_df[filtered_df["City_Type"].isin(city)]
else:
    filtered_df = filtered_df
    
anxiety = st.sidebar.multiselect(
    "Select Range Anxiety",
    df["Range_Anxiety_Level"].unique()
)
if anxiety:
    filtered_df = filtered_df[
        filtered_df["Range_Anxiety_Level"].isin(anxiety)
    ]
car_type = st.sidebar.multiselect(
    "Select Current Car Type",
    df["Current_Car_Type"].unique()
)
if car_type:
    filtered_df = filtered_df[
        filtered_df["Current_Car_Type"].isin(car_type)
    ]    
    
subsidy = st.sidebar.multiselect(
    "Subsidy Available",
    df["Subsidy_Available"].unique()
)
if subsidy:
    filtered_df = filtered_df[
        filtered_df["Subsidy_Available"].isin(subsidy)
    ]   
   
              

#KPI cards

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Total Buyers",
    filtered_df.shape[0]
)

col2.metric(
    "EV Buyers",
    filtered_df[filtered_df['Will_Buy_EV'] == 'Yes'].shape[0]
)

col3.metric(
    "EV Purchase Rate",
    (filtered_df[filtered_df['Will_Buy_EV'] == 'Yes'].shape[0] / df.shape[0]) * 100
)

col4.metric(
    "Home Charging",
    (filtered_df[filtered_df['Home_Charging_Possible'] == 'Yes'].shape[0] / df.shape[0]) * 100
)

#GRAPH CONNECTIVITY
fig1 = px.histogram(filtered_df,x = 'Will_Buy_EV',
                   color = 'Will_Buy_EV',
             title = 'Willingness to buy EV',
             color_discrete_map={'Yes':'#1F4E79', 'No':'#9DC3E6'}
           )
st.plotly_chart (fig1)

fig2=px.scatter(filtered_df,x= 'Daily_Commute_km',
           y='Annual_Income_USD',
          color = 'Will_Buy_EV', 
           title ='Daily commute Daily vs Annual Income',
            color_discrete_map={'Yes':'#B8860B', 'No':'#FFE699'}
)
st.plotly_chart (fig2)

fig3 = px.histogram(filtered_df,x= 'Range_Anxiety_Level',
                   color = 'Will_Buy_EV',      
                 title = 'Range Anxiety Level vs EV Purchase Decision',
                 color_discrete_map={'Yes':'#5B2C83', 'No':'#C9B1E8'},
                 barmode='group'
)

st.plotly_chart (fig3)

fig4 = px.histogram(
    filtered_df,
    x='Age',
    title='Age Distribution of Buyers',
    color_discrete_sequence=['#70AD47']
)

st.plotly_chart(fig4)

fig5 = px.pie(
    filtered_df,
    names='Home_Charging_Possible',
    title='Home Charging Availability',
    hole=0.4,
    color_discrete_sequence=['#008C95', '#8ED1D5']
)
st.plotly_chart(fig5)

fig6 = px.pie(
    filtered_df,
    names='Subsidy_Available',
    title='EV Subsidy Availability',
    hole=0.4,
    color_discrete_sequence=['#E67E22', '#F8C471']
)

st.plotly_chart(fig6)

fig7 = px.box(
    filtered_df,
    x='Will_Buy_EV',
    y='Annual_Income_USD',
    color='Will_Buy_EV',
    title='Income Distribution',
    color_discrete_map={'Yes':'#AD4A7B', 'No':'#E8A9C4'}
)
st.plotly_chart(fig7)

fig8 = px.box(
    filtered_df,
    x='Will_Buy_EV',
    y='Daily_Commute_km',
    color='Will_Buy_EV',
    title='Daily Commute Distance vs EV Purchase',
    color_discrete_map={'Yes':'#795548', 'No':'#C8A99A'}
)
st.plotly_chart(fig8)

fig9 = px.violin(
    filtered_df,
    x='Will_Buy_EV',
    y='Environmental_Concern_Level',
    color='Will_Buy_EV',
    title='Environmental Concern vs EV Purchase',
    color_discrete_map={'Yes':'#6A3D9A', 'No':'#CDB7E9'}
)
st.plotly_chart(fig9)

fig10 = px.box(
    filtered_df,
    x='City_Type',
    y='Annual_Income_USD',
    color='City_Type',
    title='Income Distribution by City Type',
    color_discrete_sequence=['#548235', '#A9D18E']
)
st.plotly_chart(fig10)

fig11 = px.strip(
    filtered_df,
    x='Charging_Stations_Near_Home',
    y='Will_Buy_EV',
    color='Will_Buy_EV',
    title='Charging Availability vs EV Purchase',
    color_discrete_map={'Yes':'#00796B', 'No':'#80CBC4'}
)
st.plotly_chart(fig11)

fig12 = px.pie(
    filtered_df,
    names='Current_Car_Type',
    title='Current Car Type Distribution',
    color_discrete_sequence=['#D97706', '#F6C66E', '#F9E2B3']
)
st.plotly_chart(fig12)

fig13 = px.histogram(
    filtered_df,
    x='Age',
    color='Will_Buy_EV',
    title='Age Distribution by EV Purchase Decision',
    color_discrete_map={'Yes':'#1565C0', 'No':'#90CAF9'}
)
st.plotly_chart(fig13)

fig14 = px.scatter(
    filtered_df,
    x='Age',
    y='Annual_Income_USD',
    color='Will_Buy_EV',
    title='Age vs Annual Income',
    color_discrete_map={'Yes':'#9A6700', 'No':'#F4D35E'}
)
st.plotly_chart(fig14)

fig15 = px.scatter(
    filtered_df,
    x='Charging_Stations_Near_Home',
    y='Charging_Stations_Near_Work',
    color='Will_Buy_EV',
    title='Home vs Work Charging Stations',
    color_discrete_map={'Yes':'#4527A0', 'No':'#B39DDB'}
)
st.plotly_chart(fig15)