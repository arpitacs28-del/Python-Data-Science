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
             color_discrete_map={
                                                 'Yes':'dark blue',
                                                 'No':'light blue'
                                             }
           )
st.plotly_chart (fig1)

fig2=px.scatter(filtered_df,x= 'Daily_Commute_km',
           y='Annual_Income_USD',
          color = 'Will_Buy_EV', 
           title ='Daily commute Daily vs Annual Income',
            color_discrete_map={
                                                'Yes':'dark blue',
                                                'No':'light blue'
                                            }
)
st.plotly_chart (fig2)

fig3 = px.histogram(filtered_df,x = 'Range_Anxiety_Level',
                   color = 'Will_Buy_EV',      
             title = 'Range Anxiety Level vs EV Purchase Decision',
              color_discrete_map={
                                    'Yes':'dark blue',
                                    'No':'light blue'
                                },
              barmode='group'
              
           )

st.plotly_chart (fig3)

