import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("new.csv")
add_selectbox = st.sidebar.selectbox(
    "Mikhail Napolov 231-1 PyProject",
    ("Comments", "Grade")
)

with st.sidebar:
    add_radio = st.radio(
        "What do u think about my page?",
        ("It's perfect", "It's nonsense")
    )
st.title('My data and main Plot')
st.header('DataSet:')
st.dataframe(df.head(100), height=300)

if st.button('View graph!'):
    fig = px.scatter(df, x='Total_Alcohol_PerCapita', y='Average_Happiness',
                     size="HDI", color="Region",
                     hover_name="Country",
                     hover_data=['HDI', 'HappinessScore', 'Real_GDP', 'Continent', 'Wine_PerCapita', 'Beer_PerCapita',
                                 'Spirit_PerCapita'], symbol='Hemisphere', log_x=True, size_max=10)
    st.plotly_chart(fig, use_container_width=False, sharing="streamlit", theme="streamlit")
st.info('Made by Mike (Mikhail Napolov)!')
