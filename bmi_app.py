import streamlit as st
user_high = st.number_input("กรอกส่วนสูง (cm)", min_value = 0.00 , value = 0.00)
button = st.button("enter")
