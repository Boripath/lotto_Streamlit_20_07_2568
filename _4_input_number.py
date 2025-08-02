import streamlit as st
import re

def input_numbers(bet_type, double_mode):
    st.subheader("🔢 เพิ่มตัวเลขที่จะแทง")

    # เริ่มต้นตัวแปรใน session_state
    st.session_state.setdefault("selected_numbers", [])
    st.session_state.setdefault("input_text", "")

    # ช่องกรอกเลข
    input_text = st.text_area(
        "กรอกตัวเลข (สามารถแยกด้วยช่องว่าง, คอมม่า, ขีด ฯลฯ):",
        value=st.session_state.input_text,
        height=100,
        key="input_text_area"
    )

    # ฟังก์ชันช่วย: ตัดเลขอัตโนมัติจากข้อความที่กรอก
    def extract_numbers(text, length):
        clean_text = re.sub(r"[^0-9]", "", text)
        return [clean_text[i:i+length] for i in range(0, len(clean_text), length) if len(clean_text[i:i+length]) == length]

    # ตัดเลขตาม bet_type และ double_mode
    numbers = []
    if double_mode:
        # โหมดเบิ้ล/ตอง
        if bet_type == "2 ตัว":
            numbers = [f"{i}{i}" for i in range(10)]
        elif bet_type == "3 ตัว":
            numbers = [f"{i}{i}{i}" for i in range(10)]
    else:
        if bet_type == "2 ตัว" or bet_type == "รูด" or bet_type == "19 ประตู":
            numbers = extract_numbers(input_text, 2)
        elif bet_type == "3 ตัว" or bet_type == "6 กลับ":
            numbers = extract_numbers(input_text, 3)
        elif bet_type == "วิ่ง":
            # ตัดทีละตัวเลขเดียว
            numbers = list(re.sub(r"[^0-9]", "", input_text))

    # บันทึกเลขไว้ใน session_state
    st.session_state.selected_numbers = numbers
    st.session_state.input_text = input_text

    # แสดงเลขที่แยกแล้ว + ปุ่มลบแต่ละเลข
    st.markdown("#### 📋 เลขที่กรอก")
    if numbers:
        cols = st.columns(10)
        for idx, num in enumerate(numbers):
            if cols[idx % 10].button(f"❌ {num}", key=f"del_{idx}"):
                st.session_state.selected_numbers.remove(num)
                # อัปเดตข้อความที่กรอกใหม่เป็นช่องว่างหรือเลขที่เหลือ
                st.session_state.input_text = " ".join(st.session_state.selected_numbers)
                st.experimental_rerun()
    else:
        st.info("ยังไม่มีเลขที่แยกออกมา กรุณากรอกเลขให้ครบตามประเภทที่เลือก")

    # คืนค่าเลขทั้งหมด
    return st.session_state.selected_numbers
