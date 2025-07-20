import streamlit as st

def input_price(numbers, bet_type):
    if not numbers:
        st.info("ยังไม่มีเลขที่ต้องการใส่ราคา")
        return []

    # ✅ กำหนดค่า default ราคาถ้าไม่ได้กำหนดใน session
    if "price_top" not in st.session_state:
        st.session_state.price_top = 0
    if "price_bottom" not in st.session_state:
        st.session_state.price_bottom = 0

    # ✅ ใส่ราคาบน/ล่าง และปุ่มเพิ่มบิล
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        price_top = st.number_input(
            "ใส่ราคาบน", min_value=0, step=1,
            label_visibility="collapsed", key="price_top"
        )
    with col2:
        price_bottom = st.number_input(
            "ใส่ราคาล่าง", min_value=0, step=1,
            label_visibility="collapsed", key="price_bottom"
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

        # ✅ ล้างข้อมูลเมื่อเพิ่มเสร็จ
        st.session_state.input_text = ""              # ล้างข้อความที่กรอก
        st.session_state.selected_numbers = []        # ล้างเลขที่เลือก
        st.session_state.price_top = 0                # รีเซ็ตราคาบน
        st.session_state.price_bottom = 0             # รีเซ็ตราคาล่าง
        st.session_state.editing_bill = None          # เคลียร์โหมดแก้ไข

        st.success("เพิ่มบิลเรียบร้อยแล้ว ✅")
        st.rerun()

    return bills
