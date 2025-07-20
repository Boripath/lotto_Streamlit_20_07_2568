import streamlit as st

def input_prices(selected_numbers, bet_type):
    if "bill_table" not in st.session_state:
        st.session_state.bill_table = []

    if not selected_numbers:
        st.info("กรุณากรอกเลขก่อน")
        return

    # ✅ แสดงเลขทั้งหมดในบรรทัดเดียว
    st.markdown("<h5 style='margin-bottom: 5px;'>เลขชุด:</h5>", unsafe_allow_html=True)
    st.markdown(
        f"<div style='font-size: 24px; font-weight: bold; color: #3498db;'>{' '.join(selected_numbers)}</div>",
        unsafe_allow_html=True
    )

    # ✅ ช่องใส่ราคา บน/ล่าง + ปุ่มเพิ่มบิล
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        top_price = st.number_input(
            label="ใส่ราคาบน",
            min_value=0,
            step=1,
            key="top_price_all",
            label_visibility="visible"
        )
    with col2:
        bottom_price = st.number_input(
            label="ใส่ราคาล่าง",
            min_value=0,
            step=1,
            key="bottom_price_all",
            label_visibility="visible"
        )
    with col3:
        if st.button("➕ เพิ่มบิล", key="add_all"):
            for number in selected_numbers:
                st.session_state.bill_table.append({
                    "bet_type": bet_type,
                    "number": number,
                    "top": top_price,
                    "bottom": bottom_price
                })
            st.success("เพิ่มบิลทั้งหมดสำเร็จแล้ว ✅")
            # ✅ เคลียร์ selected_numbers หลังเพิ่ม
            st.session_state.selected_numbers = []
            st.session_state.top_price_all = 0
            st.session_state.bottom_price_all = 0
