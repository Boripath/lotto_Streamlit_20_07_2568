import streamlit as st

def show_note_and_total():
    if "bills" in st.session_state and st.session_state.bills:
        total_top = sum(b.get("top", 0) for b in st.session_state.bills)
        total_bottom = sum(b.get("bottom", 0) for b in st.session_state.bills)
        total_amount = total_top + total_bottom

        st.markdown(f"<h4 style='display:inline;'>ยอดรวม: {total_amount}</h4> <span>(บาท)</span>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown("<b>บันทึกช่วยจำ</b>", unsafe_allow_html=True)
    with col2:
        st.text_area("", key="memo", height=50)
