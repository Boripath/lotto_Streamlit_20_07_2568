import streamlit as st

def select_pricerate():
    st.markdown("### ")  # ช่องว่างเล็กน้อยให้พอดีกับหัวข้อ

    # ใช้ HTML + selectbox ด้วย key เฉพาะ
    st.markdown(
        """
        <style>
        .inline-container {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .inline-label {
            font-size: 18px;
            margin-right: 5px;
        }
        </style>
        <div class='inline-container'>
            <div class='inline-label'>💸 อัตราจ่าย :</div>
        """,
        unsafe_allow_html=True
    )

    # วาง selectbox ข้างใน container
    rate = st.selectbox(
        label="",  # ไม่แสดง label ด้านบน
        options=["บาทละ 70", "บาทละ 90"],
        index=0,
        label_visibility="collapsed",
        key="rate_select"
    )

    st.markdown("</div>", unsafe_allow_html=True)  # ปิด div .inline-container

    return rate
