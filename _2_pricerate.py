import streamlit as st

def select_pricerate():
    st.markdown(
        """
        <style>
        .price-row {
            display: flex;
            align-items: center;
            font-size: 18px;
            margin-bottom: 10px;
        }
        .price-label {
            margin-right: 10px;
            white-space: nowrap;
        }
        .price-box {
            flex-grow: 1;
        }
        </style>
        <div class='price-row'>
            <div class='price-label'>💸 อัตราจ่าย :</div>
            <div class='price-box'>
        """,
        unsafe_allow_html=True
    )

    # แทรก selectbox ลงในบรรทัดเดียวกับ HTML
    rate = st.selectbox(
        label="",
        options=["บาทละ 70", "บาทละ 90"],
        index=0,
        label_visibility="collapsed",
        key="rate_select"
    )

    # ปิดแท็ก HTML ที่เปิดไว้
    st.markdown("</div></div>", unsafe_allow_html=True)

    return rate
