import streamlit as st

illegal_temperature = False

initial_unit = input("What unit is your temperature in? (F, C, or K): ")
temp = input("What temperature is it? ")
conversion_unit = input("What unit would you like to convert to? (F, C, or K): ")

if initial_unit == conversion_unit:
    print("That's the same unit!")

try:
    float(temp)
except:
    illegal_temperature = True
    print("Enter a real temperature!")
    
if illegal_temperature == False: 
    if initial_unit == "C":
        
        if conversion_unit == "F":
            converted_temp = (float(temp) * 9/5) + 32
        if conversion_unit == "K":
            converted_temp = float(temp) + 273.15 
        
    elif initial_unit == "F":
        
        if conversion_unit == "C":
            converted_temp = (float(temp) - 32) * 5/9
        if conversion_unit == "K":
            converted_temp = (float(temp) - 32) * 5/9 + 273.15
        
    elif initial_unit == "K":
        
        if conversion_unit == "F":
            converted_temp = (float(temp) -273.15) * 1.8  + 32
        if conversion_unit == "C":
            converted_temp = float(temp) - 273.15
        
    print("It is " + str(int(converted_temp)) + "°" + conversion_unit)

st.write('Weldcome to Streamlit')
