import streamlit as st
import webbrowser

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

# Tlačítko pro přesměrování na URL
if st.button("Spočítat nejlepší nabídky"):
    url = f"https://prodej.e15.cz/hypoteky/srovnani/?loan={loan_value}&type={selected_type}&leadGuid=906154c3-f656-4813-ac4d-a0592205c46d"
    webbrowser.open(url)
