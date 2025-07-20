import streamlit as st

def input_price(numbers, bet_type):
    if not numbers:
        st.info("ยังไม่มีเลขที่ต้องการใส่ราคา")
        return []

    # ✅ กำหนดค่า default ถ้ายังไม่มีใน session
    st.session_state.setdefault("price_top_value", 0)
    st.session_state.setdefault("price_bottom_value", 0)

    # ✅ ใส่ราคาบน/ล่าง และปุ่มเพิ่มบิล
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        price_top = st.number_input(
            "ใส่ราคาบน", min_value=0, step=1,
            label_visibility="collapsed", key="price_top_value"
        )
    with col2:
        price_bottom = st.number_input(
            "ใส่ราคาล่าง", min_value=0, step=1,
            label_visibility="collapsed", key="price_bottom_value"
        )
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

        if "bills" not in st.session_state:
            st.session_state.bills = []
        st.session_state.bills.extend(bills)

        # ✅ ล้างค่าโดยตั้ง flag เพื่อให้ app.py เคลียร์
        st.session_state.clear_input_fields = True

    return bills
