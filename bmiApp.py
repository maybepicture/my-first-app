import streamlit as st
st.title("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณเพื่อเช็กสุขภาพเบื้องต้น")
user_height = st.number_input("กรอกส่วนสูง (เซนติเมตร)", min_value = 0.00 , value = 0.00)
user_weigth = st.number_input("กรอกน้ำหนัก (กิโลกรัม)", min_value = 0.00 , value = 0.00)
if st.button("คำนวณค่า bmi"):
  height_m = user_height/100
  bmi = user_weigth/(height_m**2)
if bmi < 18.5:
  st.warning("คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
elif 18.5 <= bmi < 23.0:
  st.success("คุณมีน้ำหนักอยู่ในเกณฑ์ (สุขภาพดี)")
elif 23.0 <= bmi < 25.0:
  st.success("คุณมีน้ำหนักมากกว่าเกณฑ์ (ท้วม)")
else:
  st.error("คุณอยู่ในเกณฑ์อ้วน ควรระวังเรื่องสุขภาพและออกกำลังกาย")




st.header(f"(ค่า bmi ของคุณคือ: **(bmi:.2f)**") 
