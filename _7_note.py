import streamlit as st

def show_note_and_total():
    if "bills" in st.session_state and st.session_state.bills:
        total_top = sum(b.get("top", 0) for b in st.session_state.bills)
        total_bottom = sum(b.get("bottom", 0) for b in st.session_state.bills)
        total_amount = total_top + total_bottom
        st.markdown(f"<h4>ยอดรวม: {total_amount}</h4> (บาท)", unsafe_allow_html=True)

    st.text_area("บันทึกช่วยจำ", key="memo")
