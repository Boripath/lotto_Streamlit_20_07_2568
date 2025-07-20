import streamlit as st

# ✅ แสดงยอดรวมและช่องบันทึกช่วยจำในบรรทัดเดียวกันแบบสวยงาม

def show_note_and_total(total_amount):
    col1, col2 = st.columns([1, 3])

    with col1:
        st.markdown(f"<div style='font-size:18px; font-weight:bold; margin-top:6px;'>ยอดรวม: {total_amount} <span style='font-weight:normal;'>(บาท)</span></div>", unsafe_allow_html=True)

    with col2:
        st.text_input("บันทึกช่วยจำ", key="memo", label_visibility="visible", help="ใส่หมายเหตุหรือลายละเอียดเพิ่มเติมที่นี่")
