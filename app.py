import streamlit as st

# 🔹 เรียกใช้ทุกโมดูลย่อย
import _0_select_draw
import _1_header
import _2_pricerate
import _3_bet_type
import _4_input_number
import _5_input_price
import _6_bill_table
import _7_note
import _8_summary_footer

# ตั้งค่า Streamlit Layout
st.set_page_config(page_title="โพยหวยออนไลน์", page_icon="🎯", layout="wide")

# หัวเว็บและเลือกงวด
_0_select_draw.select_draw()
_1_header.render_header()

# เลือกราคาจ่าย
_2_pricerate.select_pricerate()

# เลือกประเภทการแทง + เพิ่มเลข + ใส่ราคา
bet_type, double_mode = _3_bet_type.bet_type_selector()
numbers = _4_input_number.input_numbers(bet_type, double_mode)
_5_input_price.input_price(numbers, bet_type)

# แสดงตารางบิล และยอดรวม
_6_bill_table.show_bill_table()
_7_note.show_note_and_total()

# ปุ่มล้างตาราง + บันทึกโพย
_8_summary_footer.show_summary_footer()
