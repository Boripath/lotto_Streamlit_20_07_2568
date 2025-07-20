import streamlit as st
import re
import itertools

# ✅ ฟังก์ชันสำหรับกรอกเลขและแสดงแบบ Grid แนวนอน

def input_numbers(bet_type, double_mode):
    # ✅ ป้องกัน error ถ้า session_state ไม่มี selected_numbers หรือ partial_input
    if "selected_numbers" not in st.session_state:
        st.session_state.selected_numbers = []
    if "partial_input" not in st.session_state:
        st.session_state.partial_input = ""

    # ✅ ถ้าเปิดโหมดเลขเบิ้ล/เลขตอง
    if double_mode:
        if bet_type == "2 ตัว":
            new_numbers = [f"{i}{i}" for i in range(10)]
        elif bet_type == "3 ตัว":
            new_numbers = [f"{i}{i}{i}" for i in range(10)]
        else:
            new_numbers = []
    else:
        raw_input = st.text_area("", "", height=100, label_visibility="collapsed")

        # ล้างช่องพิเศษก่อน
        raw_input = raw_input.replace("\n", "").replace(" ", "").replace(",", "").replace("/", "")
        st.session_state.partial_input += raw_input

        new_numbers = []

        if bet_type == "2 ตัว":
            while len(st.session_state.partial_input) >= 2:
                num = st.session_state.partial_input[:2]
                st.session_state.partial_input = st.session_state.partial_input[2:]
                new_numbers.append(num)
        elif bet_type == "3 ตัว":
            while len(st.session_state.partial_input) >= 3:
                num = st.session_state.partial_input[:3]
                st.session_state.partial_input = st.session_state.partial_input[3:]
                new_numbers.append(num)
        elif bet_type == "6 กลับ":
            temp_input = st.session_state.partial_input
            st.session_state.partial_input = ""  # เคลียร์เพื่อรับเลขใหม่
            for i in range(0, len(temp_input) - 2, 3):
                part = temp_input[i:i+3]
                if len(part) == 3 and part.isdigit():
                    perms = set(["".join(p) for p in itertools.permutations(part)])
                    new_numbers.extend(perms)
        else:
            if st.session_state.partial_input:
                new_numbers = [st.session_state.partial_input]
                st.session_state.partial_input = ""

    # ✅ เพิ่มเลขใหม่เข้า session_state แบบไม่ซ้ำ
    for num in new_numbers:
        if num and num not in st.session_state.selected_numbers:
            st.session_state.selected_numbers.append(num)

    # ✅ สร้าง Layout แนวนอนแบบ Wrap และคลิกเพื่อลบ
    st.markdown("""
        <style>
        .number-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 10px;
        }
        .number-box {
            background-color: #3498db;
            color: white;
            font-size: 24px;
            font-weight: bold;
            padding: 10px 18px;
            border-radius: 10px;
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

    # ✅ ใช้ Layout แนวนอนแบบ Columns
    cols = st.columns(10)
    for i, num in enumerate(st.session_state.selected_numbers.copy()):
        col = cols[i % 10]
        with col:
            if st.button(num, key=f"del_{num}"):
                st.session_state.selected_numbers.remove(num)

    return st.session_state.selected_numbers
