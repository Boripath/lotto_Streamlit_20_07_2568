import streamlit as st
import re
import itertools

def input_numbers(bet_type):
    st.markdown("### 🧮 ใส่เลขที่ต้องการแทง")

    # ✅ ช่องกรอกเลขทั้งหมด
    raw_input = st.text_area(
        label="กรอกเลข (คั่นด้วยเว้นวรรค , หรือ / ก็ได้)",
        placeholder="ตัวอย่าง: 21211331 หรือ 21,21,13,31 หรือ 123/356/789",
        height=100
    )

    numbers = []

    if raw_input:
        # ✅ แปลงข้อความเป็นรายการเลข โดยแยกด้วย , / หรือเว้นวรรค
        raw_input = raw_input.replace("\n", " ")
        split_numbers = re.split(r"[,\s/]+", raw_input.strip())

        # ✅ ตัดเลขตามประเภท
        if bet_type == "2 ตัว":
            numbers = [num[i:i+2] for num in split_numbers for i in range(0, len(num), 2) if len(num[i:i+2]) == 2]
        elif bet_type == "3 ตัว":
            numbers = [num[i:i+3] for num in split_numbers for i in range(0, len(num), 3) if len(num[i:i+3]) == 3]
        elif bet_type == "6 กลับ":
            all_permutations = set()
            for num in split_numbers:
                if len(num) == 3 and num.isdigit():
                    perms = set(["".join(p) for p in itertools.permutations(num)])
                    all_permutations.update(perms)
            numbers = sorted(all_permutations)
        else:
            numbers = split_numbers  # สำหรับ วิ่ง, รูด, 19 ประตู อื่น ๆ

    # ✅ แสดงรายการเลขที่แยกออกมาแล้ว
    if numbers:
        st.markdown("#### 🔢 เลขที่ระบบตัดออกมา:")
        st.write(", ".join(numbers))

    return numbers
