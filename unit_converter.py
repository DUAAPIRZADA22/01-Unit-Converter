import streamlit as st
import pandas as pd

def convert_units(value, from_unit, to_unit, conversion_dict):
    if from_unit in conversion_dict and to_unit in conversion_dict[from_unit]:
        return value * conversion_dict[from_unit][to_unit]
    return None

def main():
    st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
    
    # Styling for both dark and light themes
    st.markdown(
        """
        <style>
            .title {text-align: center; font-size: 36px; font-weight: bold; padding: 10px;}
            .sub-header {text-align: center; font-size: 20px; margin-bottom: 20px;}
            .footer {text-align: center; font-size: 14px; margin-top: 30px; padding: 10px;}
            .container {background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.2);}
            .button {display: flex; justify-content: center; margin-top: 20px;}
            @media (prefers-color-scheme: dark) {
                .title {color: #ffffff;}
                .sub-header {color: #aaaaaa;}
                .footer {color: #cccccc;}
                .container {background: rgba(50, 50, 50, 0.3);}
            }
            @media (prefers-color-scheme: light) {
                .title {color: #2E3A87;}
                .sub-header {color: #444;}
                .footer {color: #666;}
                .container {background: rgba(240, 240, 240, 0.7);}
            }
        </style>
        """, unsafe_allow_html=True
    )
    
    st.markdown("<h1 class='title'>🔄 Unit Converter</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Convert between different units easily!</p>", unsafe_allow_html=True)
    
    conversion_data = {
        "Length": {
            "Meters": {"Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084},
            "Kilometers": {"Meters": 1000, "Miles": 0.621371, "Feet": 3280.84},
            "Miles": {"Meters": 1609.34, "Kilometers": 1.60934, "Feet": 5280},
            "Feet": {"Meters": 0.3048, "Kilometers": 0.0003048, "Miles": 0.000189394}
        },
        "Weight": {
            "Kilograms": {"Grams": 1000, "Pounds": 2.20462},
            "Grams": {"Kilograms": 0.001, "Pounds": 0.00220462},
            "Pounds": {"Kilograms": 0.453592, "Grams": 453.592}
        },
        "Temperature": {
            "Celsius": {"Fahrenheit": lambda c: (c * 9/5) + 32, "Kelvin": lambda c: c + 273.15},
            "Fahrenheit": {"Celsius": lambda f: (f - 32) * 5/9, "Kelvin": lambda f: (f - 32) * 5/9 + 273.15},
            "Kelvin": {"Celsius": lambda k: k - 273.15, "Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32}
        }
    }
    
    with st.container():
        st.markdown("<div class='container'>", unsafe_allow_html=True)
        category = st.selectbox("Select a category:", list(conversion_data.keys()))
        from_unit = st.selectbox("Convert from:", list(conversion_data[category].keys()))
        to_unit = st.selectbox("Convert to:", list(conversion_data[category][from_unit].keys()))
        value = st.number_input("Enter the value:", min_value=0.0, step=0.1)
        st.markdown("</div>", unsafe_allow_html=True)
        
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='button'>", unsafe_allow_html=True)
        if st.button("Convert", help="Click to convert the value"):
            conversion = conversion_data[category][from_unit][to_unit]
            result = conversion(value) if callable(conversion) else value * conversion
            st.success(f"✅ {value} {from_unit} = {result:.2f} {to_unit}")
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<p class='footer'>Developed by Duaa Pirzada | <a href='https://x.com/DuaaPirzada' target='_blank'>Twitter</a> | <a href='https://www.linkedin.com/in/duaa-pirzada-52a1062aa/' target='_blank'>LinkedIn</a></p>", unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()



    
