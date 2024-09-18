import streamlit as st
from api import get_latest_rate, get_historical_rate
from frankfurter import get_currencies
from currency import format_conversion_result

# Title
st.title("FX Converter")

# Get available currencies
currencies = get_currencies()

# Input: Amount, From Currency, To Currency
amount = st.number_input("Enter the amount to be converted:", min_value=0.01, value=50.00, step=0.01)
from_currency = st.selectbox("From Currency:", currencies)
to_currency = st.selectbox("To Currency:", currencies)

# Get latest conversion rate
if st.button("Get Latest Rate"):
    rate, inverse_rate = get_latest_rate(from_currency, to_currency)
    result_text = format_conversion_result(rate, inverse_rate, amount, from_currency, to_currency, "latest")
    st.write(result_text)

# Select a date for historical rates
date = st.date_input("Select a date for historical rates:")
if st.button("Get Historical Rate"):
    rate, inverse_rate = get_historical_rate(from_currency, to_currency, date)
    result_text = format_conversion_result(rate, inverse_rate, amount, from_currency, to_currency, date)
    st.write(result_text)
