import streamlit as st

def select_pricerate():
    st.markdown("### 💸 อัตราจ่าย")

    # สร้างสองคอลัมน์: ซ้าย = label, ขวา = dropdown
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("<p style='font-size:18px; padding-top:8px;'>อัตราจ่าย :</p>", unsafe_allow_html=True)

    with col2:
        rate = st.selectbox(
            "",  # ไม่ต้องมี label
            options=["บาทละ 70", "บาทละ 90"],
            index=1
        )

    return rate
