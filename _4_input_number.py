import streamlit as st
import re
import itertools

def input_numbers(bet_type, double_mode):
    st.subheader("🔢 เพิ่มตัวเลขที่จะแทง")

    # เริ่มต้นตัวแปรใน session_state
    st.session_state.setdefault("selected_numbers", [])
    st.session_state.setdefault("input_text", "")

    # ช่องกรอกเลข
    input_text = st.text_area(
        "กรอกตัวเลข (แยกด้วยช่องว่าง, คอมม่า, ขีด ฯลฯ):",
        value=st.session_state.input_text,
        height=100,
        key="input_text_area"
    )

    def extract_numbers(text, length):
        clean_text = re.sub(r"[^0-9]", "", text)
        return [clean_text[i:i+length] for i in range(0, len(clean_text), length) if len(clean_text[i:i+length]) == length]

    numbers = []
    if double_mode:
        if bet_type == "2 ตัว":
            numbers = [f"{i}{i}" for i in range(10)]
        elif bet_type == "3 ตัว":
            numbers = [f"{i}{i}{i}" for i in range(10)]
    else:
        if bet_type == "2 ตัว" or bet_type in ["รูด", "19 ประตู"]:
            numbers = extract_numbers(input_text, 2)
        elif bet_type in ["3 ตัว"]:
            numbers = extract_numbers(input_text, 3)
        elif bet_type == "6 กลับ":
            base_numbers = extract_numbers(input_text, 3)
            numbers_set = set()
            for num in base_numbers:
                perms = set([''.join(p) for p in itertools.permutations(num)])
                numbers_set.update(perms)
            numbers = sorted(numbers_set)
        elif bet_type == "วิ่ง":
            numbers = list(re.sub(r"[^0-9]", "", input_text))

    st.session_state.selected_numbers = numbers
    st.session_state.input_text = input_text

    # แสดงเลขที่แยกได้ + ปุ่มลบ
    st.markdown("#### 📋 เลขที่กรอก")
    if numbers:
        cols = st.columns(10)
        for idx, num in enumerate(numbers):
            if cols[idx % 10].button(f"❌ {num}", key=f"del_{idx}"):
                st.session_state.selected_numbers.remove(num)
                st.session_state.input_text = " ".join(st.session_state.selected_numbers)
                st.rerun()  # 🔄 ใช้ st.rerun() แทน experimental
    else:
        st.info("ยังไม่มีเลข กรุณากรอกให้ครบตามประเภท")

    return st.session_state.selected_numbers
