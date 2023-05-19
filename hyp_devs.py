import streamlit as st

# Vložení úvodního loga
logo_image = "icon calc/finance.e15.cz_logo_500_DPI_edit.png"  # Nahraďte cestou k úvodnímu logu ve formátu PNG nebo JPG
st.image(logo_image)

# Vstupní pole pro hodnotu hypotéky
st.markdown("**HODNOTA HYPOTÉKY (v Kč)**")
loan_value = st.text_input("HODNOTA HYPOTÉKY", value="", key="loan_value", label_visibility="collapsed")

# Odstranění mezer z vstupního řetězce
loan_value = loan_value.replace(" ", "")

# Ověření, zda je vstup číslo
if loan_value.isnumeric():
    loan_value = loan_value
else:
    loan_value = 0


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

# Funkce pro aktualizaci URL
def update_url():
    global url_link
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

# Při změně hodnoty vstupního pole hypotéky nebo typu nemovitosti se automaticky aktualizuje URL
if loan_value or property_type:
    update_url()
