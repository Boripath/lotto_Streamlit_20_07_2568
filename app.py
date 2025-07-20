import streamlit as st
from _1_header import render_header
from _2_pricerate import select_pricerate
from _3_bet_type import bet_type_selector
from _4_input_number import input_numbers
from _5_input_price import input_price
from _6_bill_table import show_bill_table
st.set_page_config(page_title="โพยหวยออนไลน์", layout="centered")

# ✅ แสดงหัวเว็บ
render_header()

# ✅ เลือกอัตราจ่าย
rate = select_pricerate()

# ✅ เลือกประเภทการแทง
bet_type, double_mode = bet_type_selector()

# ✅ ใส่ตัวเลข
numbers = input_numbers(bet_type, double_mode)

# ✅ ใส่ราคา
input_price(numbers, bet_type)

# ✅ แสดงบิล
show_bill_table()
