import streamlit as st
import plotly.express as px
from backend.src.dummy_data import get_data

def home_page():
    st.title("Weather Forecast for the Next Days")
    place = st.text_input("Place: ")
    days = int(st.slider("Forecast Days", min_value=1, max_value=5,
                    help="Select the number of forecasted days"))
    option = st.selectbox("Select data to view", 
                        ("Temperature", "Sky"))
    st.subheader(f"{option} for the next {days} days in {place}")

    if place:
        dates, weather = get_data(place, days, option)
        # Plot Graph
        figure = px.line(x=dates, y=weather, labels={
            "X":"Dates",
            "Y":"Temperatures (C)"
        })
        st.plotly_chart(figure)