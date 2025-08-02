import streamlit as st

def input_price(numbers, bet_type):
    if not numbers:
        st.warning("⚠️ ยังไม่มีเลข กรุณากรอกเลขก่อนเพิ่มบิล")
        return []

    st.subheader("💰 ใส่ราคาแต่ละบิล")

    # กำหนด default session_state
    st.session_state.setdefault("price_top_value", 0)
    st.session_state.setdefault("price_bottom_value", 0)
    st.session_state.setdefault("price_tod_value", 0)

    # Layout ช่องใส่ราคาตามประเภทการแทง
    cols = st.columns([1, 1, 1])
    with cols[0]:
        price_top = st.number_input("ราคาบน", min_value=0, step=1, key="price_top_value")
    with cols[1]:
        price_bottom = st.number_input("ราคาล่าง", min_value=0, step=1, key="price_bottom_value")

    price_tod = 0
    if bet_type in ["3 ตัว", "6 กลับ"]:
        with cols[2]:
            price_tod = st.number_input("ราคาโต๊ด", min_value=0, step=1, key="price_tod_value")
    else:
        with cols[2]:
            st.markdown("ราคาโต๊ด (เฉพาะ 3 ตัว)", unsafe_allow_html=True)

    # ปุ่มเพิ่มบิล
    st.markdown("---")
    add_bill_btn = st.button("➕ เพิ่มบิล", use_container_width=True)

    bills = []
    if add_bill_btn:
        if price_top == 0 and price_bottom == 0 and price_tod == 0:
            st.error("⚠️ กรุณาใส่ราคาอย่างน้อย 1 ช่อง")
            return []

        for number in numbers:
            bill = {
                "type": bet_type,
                "number": number,
                "top": price_top,
                "bottom": price_bottom,
                "tod": price_tod
            }
            bills.append(bill)

        # บันทึกลง session_state["bills"]
        st.session_state.setdefault("bills", [])
        st.session_state.bills.extend(bills)

        # ตั้ง flag ให้เคลียร์ข้อมูลที่กรอก
        st.session_state.clear_input_fields = True

        st.success(f"✅ เพิ่มบิลจำนวน {len(bills)} รายการเรียบร้อยแล้ว!")

    return bills
