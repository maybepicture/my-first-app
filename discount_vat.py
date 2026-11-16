import streamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7% และส่วนลด")
price = st.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0 , value=0.0)
discount = st.number_input("กรอกส่วนลด", min_value=0.0, max_value=100.0, value=0.0)
discount_price = price * discount/100
vat = price * 0.07
net_price = price - discount_price + vat
st.header(f"• ส่วนลด ({discount}): -{discount_price:.2f} บาท")
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **+{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
st.divider()
st.write("นาย ณัฏฐชัย อนันต์เดชาวงษ์ เลขที่ 16 ม.4/5")
