import streamlit as st
from _1_header import render_header
from _2_pricerate import select_pricerate
from _3_bet_type import bet_type_selector
from _4_input_number import input_numbers
from _5_input_price import input_price
from _6_bill_table import show_bill_table
from _7_note import show_note_and_total
from _8_summary_footer import show_summary_footer

st.set_page_config(page_title="โพยหวยออนไลน์", layout="centered")

# ✅ แสดงหัวเว็บ
render_header()

# ✅ เลือกอัตราจ่าย
rate = select_pricerate()

# ✅ เลือกประเภทการแทง
bet_type, double_mode = bet_type_selector()

# ✅ เคลียร์ input fields หากมี flag
if st.session_state.get("clear_input_fields"):
    st.session_state.input_text = ""
    st.session_state.selected_numbers = []
    st.session_state.price_top_value = 0
    st.session_state.price_bottom_value = 0
    st.session_state.clear_input_fields = False  # reset flag
  
# ✅ ใส่ตัวเลข
numbers = input_numbers(bet_type, double_mode)

# ✅ ใส่ราคา
input_price(numbers, bet_type)

# ✅ แสดงบิล
show_bill_table()

# ✅ แสดงโน้ตและยอดรวม
show_note_and_total()

# ✅ แสดงปุ่มส่งโพย
show_summary_footer()
