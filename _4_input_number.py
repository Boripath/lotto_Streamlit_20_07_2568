import streamlit as st
import re

# ✅ ฟังก์ชันสำหรับใส่เลข และแสดงเลขที่แยกออกมา

def input_numbers(bet_type, double_mode):
    # ✅ สร้างตัวแปรใน session_state ถ้ายังไม่มี
    st.session_state.setdefault("selected_numbers", [])
    st.session_state.setdefault("input_text", "")

    # ✅ ช่องกรอกเลข
    st.markdown("<b>กรอกเลข:</b>", unsafe_allow_html=True)
    input_text = st.text_input("", value=st.session_state.input_text, key="input_text")

    # ✅ ตัดเลขอัตโนมัติจาก input_text
    numbers = []
    clean_text = re.sub(r"[^0-9]", "", input_text)

    if double_mode:
        # โหมดเบิ้ล/ตอง
        if bet_type == "2 ตัว":
            numbers = [f"{i}{i}" for i in range(10)]
        elif bet_type == "3 ตัว":
            numbers = [f"{i}{i}{i}" for i in range(10)]
    else:
        if bet_type == "2 ตัว":
            numbers = [clean_text[i:i+2] for i in range(0, len(clean_text), 2) if len(clean_text[i:i+2]) == 2]
        elif bet_type == "3 ตัว" or bet_type == "6 กลับ":
            numbers = [clean_text[i:i+3] for i in range(0, len(clean_text), 3) if len(clean_text[i:i+3]) == 3]

    # ✅ บันทึกเลขที่แยกได้
    st.session_state.selected_numbers = numbers

    # ✅ แสดงเลขที่แยกได้ (คลิกลบทีละตัว)
    st.markdown("<b>เลขที่กรอก:</b>", unsafe_allow_html=True)
    cols = st.columns(10)
    for idx, num in enumerate(numbers):
        if cols[idx % 10].button(num, key=f"del_{idx}"):
            st.session_state.selected_numbers.remove(num)
            st.session_state.input_text = " ".join(st.session_state.selected_numbers)
            st.experimental_rerun()

    return numbers
