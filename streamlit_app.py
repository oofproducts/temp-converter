import streamlit as st

illegal_temperature = False

initial_unit = st.radio(
    "What is the starting unit of your temperature?",
    ["Celsius", "Fahrenheit", "Kelvin"],)

st.write('Weleedeewxxxeeeecome to Streamlit')
