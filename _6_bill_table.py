import streamlit as st

def show_bill_table():
    st.subheader("🧾 ตารางบิลทั้งหมด")

    if "bills" not in st.session_state or not st.session_state.bills:
        st.info("ยังไม่มีบิลที่เพิ่มเข้ามา")
        return

    total_amount = 0

    # แสดงบิลทีละแถว
    for idx, bill in enumerate(st.session_state.bills):
        bet_type = bill.get("type", "")
        number = bill.get("number", "")
        top = bill.get("top", 0)
        bottom = bill.get("bottom", 0)
        tod = bill.get("tod", 0)

        amount = top + bottom + tod
        total_amount += amount

        cols = st.columns([3, 2, 2, 1, 1])
        with cols[0]:
            st.markdown(f"**{bet_type}** : {number}")
        with cols[1]:
            st.markdown(f"บน: {top}")
        with cols[2]:
            st.markdown(f"ล่าง: {bottom} | โต๊ด: {tod}")
        with cols[3]:
            if st.button("✏️ แก้ไข", key=f"edit_{idx}"):
                # โหลดข้อมูลกลับไปยัง input
                st.session_state.selected_numbers = [number]
                st.session_state.input_text = number
                st.session_state.price_top_value = top
                st.session_state.price_bottom_value = bottom
                st.session_state.price_tod_value = tod
                st.session_state.edit_mode = True
                st.session_state.edit_index = idx
                st.experimental_rerun()
        with cols[4]:
            if st.button("🗑️ ลบ", key=f"delete_{idx}"):
                st.session_state.bills.pop(idx)
                st.success(f"🗑️ ลบบิล {number} เรียบร้อยแล้ว")
                st.experimental_rerun()

    # แสดงยอดรวม
    st.markdown("---")
    st.success(f"💵 ยอดรวมทั้งหมด: {total_amount} บาท")
