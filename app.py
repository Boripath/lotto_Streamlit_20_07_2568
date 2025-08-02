import streamlit as st
from _0_select_draw import select_draw
from _1_header import render_header
from _2_pricerate import select_pricerate
from _3_bet_type import bet_type_selector
from _4_input_number import input_numbers
from _5_input_price import input_price
from _6_bill_table import show_bill_table
from _7_note import show_note_and_total
from _8_summary_footer import show_summary_footer

# ✅ ตั้งค่าเว็บเบื้องต้น
st.set_page_config(page_title="โพยหวยออนไลน์", layout="centered")

# ✅ เลือกงวดหวย + นับถอยหลัง
select_draw()

# ✅ แสดงหัวเว็บ (ชื่อหวย + ธงชาติ + เวลานับถอยหลัง)
render_header()

# ✅ เลือกราคาจ่าย
select_pricerate()

# ✅ เลือกประเภทการแทง + โหมดเบิ้ล/ตอง
bet_type, double_mode = bet_type_selector()

# ✅ ตรวจและเคลียร์ช่อง input หากเพิ่มบิลแล้ว
if st.session_state.get("clear_input_fields", False):
    st.session_state.input_text = ""
    st.session_state.selected_numbers = []
    st.session_state.price_top_value = 0
    st.session_state.price_bottom_value = 0
    st.session_state.price_tod_value = 0
    st.session_state.clear_input_fields = False
    st.session_state.edit_mode = False
    st.session_state.edit_index = None
    st.experimental_rerun()

# ✅ กรอกเลข
numbers = input_numbers(bet_type, double_mode)

# ✅ เพิ่มบิลใหม่ หรือแก้ไขบิลเดิม
from datetime import datetime
if numbers:
    import streamlit as st
    from _5_input_price import input_price

    # รับราคาและกดปุ่มเพิ่มบิล
    bills_added = input_price(numbers, bet_type)

    # ถ้ามี flag edit_mode → แก้ไขบิลเดิมแทนเพิ่มใหม่
    if st.session_state.get("edit_mode", False) and bills_added:
        idx = st.session_state.get("edit_index")
        if idx is not None and idx < len(st.session_state.bills):
            st.session_state.bills[idx] = bills_added[0]  # แทนที่บิลเก่า
            st.success(f"✏️ แก้ไขบิล {bills_added[0]['number']} สำเร็จแล้ว!")
            st.session_state.edit_mode = False
            st.session_state.edit_index = None
            st.session_state.clear_input_fields = True
            st.experimental_rerun()

# ✅ แสดงตารางบิลทั้งหมด
show_bill_table()

# ✅ บันทึกช่วยจำ + ยอดรวม
show_note_and_total()

# ✅ ปุ่มบันทึก Google Sheet และล้างโพย
show_summary_footer()
