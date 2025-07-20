import streamlit as st

def select_pricerate():
    # ใช้ HTML และ Streamlit columns เพื่อจัด layout แนวนอนแบบมืออาชีพ
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("<p style='font-size:18px; padding-top:6px;'>💸 อัตราจ่าย :</p>", unsafe_allow_html=True)

    with col2:
        rate = st.selectbox(
            label=" ",  # เว้นว่างเพื่อไม่แสดง label ซ้ำ
            options=["บาทละ 70", "บาทละ 90"],
            index=1,
            label_visibility="collapsed"
        )

    return rate
