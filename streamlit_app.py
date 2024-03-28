import streamlit as st

illegal_temperature = False

temp = st.number_input('What is your temperature?')

initial_unit = st.radio(
    "What is the starting unit of your temperature?",
    ["Celsius", "Fahrenheit", "Kelvin"],)

conversion_unit = st.radio(
    "What unit would you like to convert to?",
    ["Celsius", "Fahrenheit", "Kelvin"],)

st.write('Weleedeewxxxeeeecome to Streamlit')
