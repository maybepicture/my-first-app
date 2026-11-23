import streamlit as st
st.title("HI")
user_high = st.number_input("กรอกส่วนสูง (cm)", min_value = 0.00 , value = 0.00)

if st.button("คำนวณค่า bmi"):
  st.title("yo")
