import streamlit as st
import re
import itertools
from safe_utils import safe_rerun

def input_numbers(bet_type, double_mode):
    st.subheader("🔢 เพิ่มตัวเลขที่จะแทง")
    st.session_state.setdefault("selected_numbers", [])
    st.session_state.setdefault("input_text", "")

    input_text = st.text_area("กรอกตัวเลข", value=st.session_state.input_text, height=100, key="input_text_area")

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
        if bet_type in ["2 ตัว", "รูด", "19 ประตู"]:
            numbers = extract_numbers(input_text, 2)
        elif bet_type == "3 ตัว":
            numbers = extract_numbers(input_text, 3)
        elif bet_type == "6 กลับ":
            raw = extract_numbers(input_text, 3)
            all_nums = set()
            for num in raw:
                perms = set("".join(p) for p in itertools.permutations(num))
                all_nums.update(perms)
            numbers = sorted(all_nums)
        elif bet_type == "วิ่ง":
            numbers = list(re.sub(r"[^0-9]", "", input_text))

    st.session_state.selected_numbers = numbers
    st.session_state.input_text = input_text

    st.markdown("#### 📋 เลขที่กรอก")
    if numbers:
        cols = st.columns(10)
        for idx, num in enumerate(numbers):
            if cols[idx % 10].button(f"❌ {num}", key=f"del_{idx}"):
                st.session_state.selected_numbers.remove(num)
                st.session_state.input_text = " ".join(st.session_state.selected_numbers)
                safe_rerun()
    else:
        st.info("ยังไม่มีเลข กรุณากรอกเลขให้ถูกต้อง")

    return st.session_state.selected_numbers
