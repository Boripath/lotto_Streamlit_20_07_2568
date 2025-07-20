import streamlit as st
import re
import itertools

def input_numbers(bet_type, double_mode):
    if "selected_numbers" not in st.session_state:
        st.session_state.selected_numbers = []

    if double_mode:
        if bet_type == "2 ตัว":
            split_numbers = [f"{i}{i}" for i in range(10)]
        elif bet_type == "3 ตัว":
            split_numbers = [f"{i}{i}{i}" for i in range(10)]
        else:
            split_numbers = []
        new_numbers = split_numbers
    else:
        raw_input = st.text_area(
            label="",
            placeholder="กรอกเลข เช่น 21211331 หรือ 21,13,31 หรือ 123/456/789",
            height=100,
            label_visibility="collapsed"
        )
        raw_input = raw_input.replace("\n", " ")
        split_raw = re.split(r"[,\s/]+", raw_input.strip())

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

    for num in new_numbers:
        if num not in st.session_state.selected_numbers:
            st.session_state.selected_numbers.append(num)

    # ✅ CSS Grid ปรับให้เรียงไปทางขวา (Wrap เมื่อยาว)
    st.markdown("""
        <style>
        .number-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 12px;
        }
        .number-btn {
            background-color: #3498db;
            color: white;
            font-weight: bold;
            padding: 8px 16px;
            font-size: 20px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
        }
        .number-btn:hover {
            background-color: #217dbb;
        }
        </style>
    """, unsafe_allow_html=True)

    # ✅ แสดงเลขเป็นปุ่มลบแบบแถวแนวนอน
    st.markdown('<div class="number-grid">', unsafe_allow_html=True)
    for num in st.session_state.selected_numbers.copy():
        # ใช้ HTML + JS workaround สำหรับคลิกลบเลข
        if st.button(f"{num}", key=f"btn_{num}", use_container_width=False):
            st.session_state.selected_numbers.remove(num)
    st.markdown('</div>', unsafe_allow_html=True)

    return st.session_state.selected_numbers
