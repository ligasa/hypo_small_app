import streamlit as st
import re

# Vložení úvodního loga
logo_image = "icon calc/finance.e15.cz_logo_500_DPI_edit.png"  # Nahraďte cestou k úvodnímu logu ve formátu PNG nebo JPG
st.image(logo_image)

# Funkce pro aktualizaci URL
def update_url():
    global url_link
    url_link = f"https://prodej.e15.cz/hypoteky/srovnani/?loan={loan_value}&type={selected_type}"

# Vstupní pole pro hodnotu hypotéky
st.markdown("**HODNOTA HYPOTÉKY (v Kč)**")
loan_value_input = st.text_input("HODNOTA HYPOTÉKY", value="", key="loan_value", label_visibility="collapsed")

# Initialize loan_value to None
loan_value = None

# Parse the input value and update loan_value
if loan_value_input:
    loan_value = int(''.join(re.findall(r'\d', loan_value_input)))

# Změna barvy vstupního pole
loan_value_style = """
    <style>
        .stTextInput input {
            background-color: #E0F0FA;
        }
    </style>
"""
st.markdown(loan_value_style, unsafe_allow_html=True)

# Radio button pro výběr typu nemovitosti
st.markdown("**TYP NEMOVITOSTI**")
property_type = st.radio("TYP NEMOVITOSTI", ["Dům", "Byt", "Nevím"], label_visibility="collapsed")

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

# Přiřazení číselné hodnoty typu nemovitosti
type_mapping = {"Dům": "0", "Byt": "1", "Nevím": "2"}
selected_type = type_mapping[property_type]

# Inicializace URL
update_url()

# Tlačítko
button_html = f'''
    <a href="{url_link}">
        <button style="
            fontWeight: 400;
            padding: 0.25rem 0.75rem;
            borderRadius: 0.25rem;
            margin: 0px;
            lineHeight: 1.6;
            width: auto;
            userSelect: none;
            backgroundColor: #FA595D;
            color: #FFFFFF;
            border: 1px solid rgba(49, 51, 63, 0.2);
            border-color: #FFFFFF"
        >
            {'Spočítat nejlepší nabídky'}
        </button>
    </a>
'''

st.markdown(button_html, unsafe_allow_html=True)
