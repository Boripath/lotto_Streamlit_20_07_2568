import streamlit as st
import re
import itertools

def input_numbers(bet_type, double_mode):
    # ✅ ถ้าเปิดเบิ้ล/ตอง ให้ auto-fill ตัวเลขเบิ้ล
    if double_mode:
        if bet_type == "2 ตัว":
            split_numbers = [f"{i}{i}" for i in range(10)]  # 11,22,...,99
        elif bet_type == "3 ตัว":
            split_numbers = [f"{i}{i}{i}" for i in range(10)]  # 111,222,...,999
        else:
            split_numbers = []
        raw_input = " ".join(split_numbers)
    else:
        # ✅ กรณีกรอกเอง
        raw_input = st.text_area(
            label="",
            placeholder="กรอกเลข เช่น 21211331 หรือ 21,13,31 หรือ 123/456/789",
            height=100,
            label_visibility="collapsed"
        )

    numbers = []

    if raw_input:
        raw_input = raw_input.replace("\n", " ")
        split_raw = re.split(r"[,\s/]+", raw_input.strip())

        # ✅ ตัดเลขตามประเภท
        if bet_type == "2 ตัว":
            numbers = [num[i:i+2] for num in split_raw for i in range(0, len(num), 2) if len(num[i:i+2]) == 2]
        elif bet_type == "3 ตัว":
            numbers = [num[i:i+3] for num in split_raw for i in range(0, len(num), 3) if len(num[i:i+3]) == 3]
        elif bet_type == "6 กลับ":
            all_perms = set()
            for num in split_raw:
                if len(num) == 3 and num.isdigit():
                    perms = set(["".join(p) for p in itertools.permutations(num)])
                    all_perms.update(perms)
            numbers = sorted(all_perms)
        else:
            numbers = split_raw  # สำหรับวิ่ง/รูด/19ประตู

    # ✅ แสดงเลขที่ได้จากการประมวลผล
    if numbers:
        st.markdown("#### 🔢 เลขที่ระบบแยกออกมา:")
        st.write(", ".join(numbers))

    return numbers
