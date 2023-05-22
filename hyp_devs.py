import streamlit as st


def update_url_and_open_page():
    global url_link
    url_link = f"https://prodej.e15.cz/hypoteky/srovnani/?loan={loan_value}&type={selected_type}"
    st.session_state.selected_type = selected_type
    open_page(url_link)


def open_page(url):
    open_script = f"""
        <script type="text/javascript">
            window.open('{url}', '_blank').focus();
        </script>
    """
    st.components.v1.html(open_script)


# Vložení úvodního loga
logo_image = "icon calc/finance.e15.cz_logo_500_DPI_edit.png"  # Nahraďte cestou k úvodnímu logu ve formátu PNG nebo JPG
st.image(logo_image)

# Vstupní pole pro hodnotu hypotéky
st.markdown("**HODNOTA HYPOTÉKY (v Kč)**")
loan_value = st.text_input("HODNOTA HYPOTÉKY", value="", key="loan_value", label_visibility="collapsed")

# Odstranění mezer z vstupního řetězce
loan_value = loan_value.replace(" ", "")

# Ověření, zda je vstup číslo
loan_value = int(loan_value) if loan_value.isdigit() else 0

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
type_mapping = {"Dům": 0, "Byt": 1, "Nevím": 2}
selected_type = type_mapping[property_type]

# Přiřazení selected_type do session_state
st.session_state.selected_type = selected_type

# Button to calculate the best offers and navigate to the URL
button_text = 'Spočítat nejlepší nabídky'
st.button(button_text, on_click=update_url_and_open_page)
