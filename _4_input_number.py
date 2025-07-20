import streamlit as st
import re
import itertools

# ใช้ SessionState เก็บเลขที่เลือกไว้
if "selected_numbers" not in st.session_state:
    st.session_state.selected_numbers = []

def input_numbers(bet_type, double_mode):
    # ✅ ถ้าเปิดโหมดเลขเบิ้ล/เลขตอง
    if double_mode:
        if bet_type == "2 ตัว":
            new_numbers = [f"{i}{i}" for i in range(10)]
        elif bet_type == "3 ตัว":
            new_numbers = [f"{i}{i}{i}" for i in range(10)]
        else:
            new_numbers = []
    else:
        raw_input = st.text_area(
            label="",
            placeholder="กรอกเลข เช่น 21211331 หรือ 21,13,31 หรือ 123/456/789",
            height=100,
            label_visibility="collapsed"
        )
        raw_input = raw_input.replace("\n", " ")
        split_raw = re.split(r'[\s,/]+', raw_input.strip())


        if bet_type == "2 ตัว":
            new_numbers = [num[i:i+2] for num in split_raw for i in range(0, len(num), 2) if len(num[i:i+2]) == 2]
        elif bet_type == "3 ตัว":
            new_numbers = [num[i:i+3] for num in split_raw for i in range(0, len(num), 3) if len(num[i:i+3]) == 3]
        elif bet_type == "6 กลับ":
            all_perms = set()
            for num in split_raw:
                if len(num) == 3 and num.isdigit():
                    perms = set(["".join(p) for p in itertools.permutations(num)])
                    all_perms.update(perms)
            new_numbers = sorted(all_perms)
        else:
            new_numbers = split_raw

    # เพิ่มเลขใหม่เข้า session_state
    for num in new_numbers:
        if num and num not in st.session_state.selected_numbers:
            st.session_state.selected_numbers.append(num)

    # ✅ แสดงตัวเลขแบบแนวนอนหลายแถว (wrap) พร้อมลบเมื่อคลิก
    st.markdown("""
        <style>
        .grid-box {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 10px;
        }
        .grid-item {
            background-color: #3498db;
            color: white;
            font-size: 20px;
            font-weight: bold;
            padding: 6px 12px;
            border-radius: 8px;
            cursor: pointer;
            border: none;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="grid-box">', unsafe_allow_html=True)
    cols = st.columns(10)  # สร้าง column เผื่อ layout
    for i, num in enumerate(st.session_state.selected_numbers.copy()):
        col = cols[i % 10]
        with col:
            if st.button(num, key=f"del_{num}"):
                st.session_state.selected_numbers.remove(num)
    st.markdown('</div>', unsafe_allow_html=True)

    return st.session_state.selected_numbers
