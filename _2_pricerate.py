import streamlit as st

def select_pricerate():
    st.markdown(
        """
        <style>
        .price-container {
            font-size: 18px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        select {
            font-size: 16px;
            padding: 5px 10px;
            border-radius: 5px;
        }
        </style>
        <div class="price-container">
            <label>💸 อัตราจ่าย :</label>
            <select id="price-rate" name="price-rate">
                <option value="70">บาทละ 70</option>
                <option value="90" selected>บาทละ 90</option>
            </select>
        </div>
        """,
        unsafe_allow_html=True
    )

    # NOTE: ไม่สามารถใช้ HTML dropdown ร่วมกับ Python logic ได้โดยตรงใน Streamlit
    # ถ้าต้องการเก็บค่า rate จริง ต้องใช้ selectbox ซ่อน แล้วจัด layout ด้วย work-around
