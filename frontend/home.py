import streamlit as st
import plotly.express as px
from backend.src.API_data import get_data

# CONSTANTS
IMAGE_PATH = "frontend/src/images/"


def home_page():
    st.title("Weather Forecast for the Next Days")
    place = st.text_input("Place: ")
    days = int(st.slider("Forecast Days", min_value=1, max_value=5,
                    help="Select the number of forecasted days"))
    option = st.selectbox("Select data to view", 
                        ("Temperature", "Sky"))
    st.subheader(f"{option} for the next {days} days in {place}")

    if place:
        try:
            weather_data = get_data(place, days)
            # Plot Graph
            if option == "Temperature":
                temperature = [temp["main"]["temp"]/10 for temp in weather_data]
                dates = [date["dt_txt"] for date in weather_data]
                figure = px.line(x=dates, y=temperature, labels={
                    "X":"Dates",
                    "Y":"Temperatures (C)"
                })
                st.plotly_chart(figure)
            elif option == "Sky":
                weather = [sky["weather"][0]["main"] for sky in weather_data]
                images_paths = [f"{IMAGE_PATH}{sky.lower()}.png" for sky in weather]
                st.image(images_paths,width=100)
        except KeyError:
            st.text("Not Existing Place")