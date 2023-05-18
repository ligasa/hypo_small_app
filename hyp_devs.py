import streamlit as st

# Vložení úvodního loga
logo_image = "icon calc/finance_e15_cz_logo.png"  # Nahraďte cestou k úvodnímu logu ve formátu PNG nebo JPG
st.image(logo_image, width=200)

# Vstupní pole pro hodnotu hypotéky
loan_value = st.number_input("HODNOTA HYPOTÉKY (v Kč)", step=1, format="%d")

# Radio button pro výběr typu nemovitosti
property_type = st.radio("TYP NEMOVITOSTI", ["Dům", "Byt", "Nevím"])

# Přiřazení číselné hodnoty typu nemovitosti
type_mapping = {"Dům": 0, "Byt": 1, "Nevím": 2}
selected_type = type_mapping[property_type]

url_link = f"https://prodej.e15.cz/hypoteky/srovnani/?loan={loan_value}&type={selected_type}"

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




