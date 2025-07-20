import streamlit as st

# ✅ ฟังก์ชันสำหรับใส่ราคาบน/ล่าง และเพิ่มบิลสำหรับเลขทั้งหมด

def input_price(numbers, bet_type):
    if not numbers:
        st.info("ยังไม่มีเลขที่ต้องการใส่ราคา")
        return []

    # ✅ จัดเรียงเลขให้อยู่ในแถวเดียวกัน
    st.markdown(
        f"""
        <div style='font-size:22px; font-weight:bold; color:#2980b9; margin-bottom:10px;'>
            {' '.join(numbers)}
        </div>
        """,
        unsafe_allow_html=True
    )

    # ✅ ใส่ราคาบน/ล่าง บรรทัดเดียวกัน + ปุ่มเพิ่มบิล
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        price_top = st.number_input("ใส่ราคาบน", min_value=0, step=1, label_visibility="collapsed", key="price_top")
    with col2:
        price_bottom = st.number_input("ใส่ราคาล่าง", min_value=0, step=1, label_visibility="collapsed", key="price_bottom")
    with col3:
        add_bill = st.button("➕ เพิ่มบิล", use_container_width=True)

    bills = []
    if add_bill:
        for number in numbers:
            bills.append({
                "type": bet_type,
                "number": number,
                "top": price_top,
                "bottom": price_bottom
            })
        st.session_state.selected_numbers.clear()

    return bills
