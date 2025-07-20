import streamlit as st

def show_bill_table():
    if "bills" not in st.session_state:
        st.session_state.bills = []

    st.markdown("### 🧾 บิลที่เพิ่มเข้ามา")
    
    if not st.session_state.bills:
        st.info("ยังไม่มีบิลในรายการ")
        return

    for idx, bill in enumerate(st.session_state.bills):
        col1, col2, col3, col4, col5 = st.columns([1.2, 1.2, 1, 1, 1])
        with col1:
            st.write(f"📌 ประเภท: **{bill['type']}**")
        with col2:
            st.write(f"🔢 เลข: **{bill['number']}**")
        with col3:
            st.write(f"⬆️ บน: **{bill['top']}**")
        with col4:
            st.write(f"⬇️ ล่าง: **{bill['bottom']}**")
        with col5:
            col_edit, col_delete = st.columns([1, 1])
            with col_edit:
                if st.button("📝", key=f"edit_{idx}"):
                    st.warning("ฟีเจอร์แก้ไขยังไม่ได้เปิดใช้งาน")
            with col_delete:
                if st.button("❌", key=f"delete_{idx}"):
                    st.session_state.bills.pop(idx)
                    st.experimental_rerun()

