import streamlit as st

def select_pricerate():
    st.subheader("💸 เลือกอัตราจ่าย")

    # ค่า default: หากยังไม่มีใน session_state ให้ใช้ 90
    default_rate = st.session_state.get("price_rate", 90)

    # radio button สำหรับเลือกราคาจ่าย
    price_rate = st.radio(
        "เลือกอัตราจ่าย",
        options=[70, 90],
        index=1 if default_rate == 90 else 0,
        format_func=lambda x: f"บาทละ {x}",
        key="price_rate_radio"
    )

    # เก็บค่าที่เลือกไว้ใน session_state
    st.session_state["price_rate"] = price_rate

    # แสดงข้อความยืนยัน (optional)
    st.success(f"📌 อัตราจ่ายที่เลือก: บาทละ {price_rate}")
