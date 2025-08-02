import streamlit as st
from _1_header import render_header
from _2_pricerate import select_pricerate
from _3_bet_type import bet_type_selector
from _4_input_number import input_numbers
from _5_input_price import input_price
from _6_bill_table import show_bill_table
from _7_note import show_note_and_total
from _8_summary_footer import show_summary_footer

# ✅ ตั้งค่าเบื้องต้นของเว็บ
st.set_page_config(page_title="โพยหวยออนไลน์", layout="centered")

# ✅ แสดงหัวเว็บ
render_header()

# ✅ เลือกอัตราจ่าย
rate = select_pricerate()

# ✅ เลือกประเภทการแทง และโหมดเลขเบิ้ล/ตอง
bet_type, double_mode = bet_type_selector()

# ✅ เคลียร์ input fields หากมี flag (จากการเพิ่มบิล / ล้างตาราง)
if st.session_state.get("clear_input_fields"):
    st.session_state.input_text = ""                 # ล้างช่องกรอกเลข
    st.session_state.selected_numbers = []          # ล้างเลขที่เลือก
    st.session_state.price_top_value = 0            # ล้างราคาบน
    st.session_state.price_bottom_value = 0         # ล้างราคาล่าง
    st.session_state.clear_input_fields = False     # รีเซ็ต flag

# ✅ กรอกเลข
numbers = input_numbers(bet_type, double_mode)

# ✅ กรอกราคา
input_price(numbers, bet_type)

# ✅ แสดงตารางบิล
show_bill_table()

# ✅ แสดงบันทึกช่วยจำ + ยอดรวม
show_note_and_total()

# ✅ แสดงปุ่มบันทึกและล้างโพย
show_summary_footer()
