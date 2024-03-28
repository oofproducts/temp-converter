import streamlit as st

temp = st.number_input('What is your temperature?')

initial_unit = st.radio(
    "What is the starting unit of your temperature?",
    ["Celsius", "Fahrenheit", "Kelvin"],)

conversion_unit = st.radio(
    "What unit would you like to convert to?",
    ["Celsius", "Fahrenheit", "Kelvin"],)

if initial_unit == conversion_unit:
    st.write('Weleedeewxxxeeeecome to Streamlit')

if initial_unit == "Celsius":
        
    if conversion_unit == "Fahrenheit":
            converted_temp = (float(temp) * 9/5) + 32
    if conversion_unit == "Kelvin":
            converted_temp = float(temp) + 273.15 
        
elif initial_unit == "Fahrenheit":
    if conversion_unit == "Celsius":
            converted_temp = (float(temp) - 32) * 5/9
    if conversion_unit == "Kelvin":
            converted_temp = (float(temp) - 32) * 5/9 + 273.15
        
elif initial_unit == "Kelvin":
        
    if conversion_unit == "Fahrenheit":
            converted_temp = (float(temp) -273.15) * 1.8  + 32
    if conversion_unit == "Celsius":
            converted_temp = float(temp) - 273.15
        
st.write(f'''It is {str(int(converted_temp))} {conversion_unit}''')