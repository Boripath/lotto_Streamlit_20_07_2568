import streamlit as st

def select_pricerate():
    # ใช้ columns + style ปรับให้หัวข้อกับ dropdown อยู่บรรทัดเดียวกัน และเท่ากัน
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("<div style='font-size:18px; padding-top:8px;'>💸 อัตราจ่าย :</div>", unsafe_allow_html=True)

    with col2:
        rate = st.selectbox(
            label="",  # ซ่อน label ดรอปดาวน์
            options=["บาทละ 70", "บาทละ 90"],
            index=1,
            key="pricerate"
        )

    return rate
