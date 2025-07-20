import streamlit as st
import re
import itertools

# ✅ ฟังก์ชันสำหรับกรอกเลขและแสดงแบบ Grid แนวนอน

def input_numbers(bet_type, double_mode):
    # ✅ ป้องกัน error ถ้า session_state ไม่มี selected_numbers
    if "selected_numbers" not in st.session_state:
        st.session_state.selected_numbers = []

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
        split_raw = re.split(r"[\s,/"]+", raw_input.strip())

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

    # ✅ ใช้ HTML กับ st.button คลุมตัวเลขทั้งหมด
    st.markdown('<div class="number-grid">', unsafe_allow_html=True)
    cols = st.columns(10)
    for i, num in enumerate(st.session_state.selected_numbers.copy()):
        col = cols[i % 10]
        with col:
            if st.button(num, key=f"del_{num}"):
                st.session_state.selected_numbers.remove(num)
    st.markdown('</div>', unsafe_allow_html=True)

    return st.session_state.selected_numbers
