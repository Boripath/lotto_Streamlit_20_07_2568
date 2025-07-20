import streamlit as st

# ✅ ปุ่มล้างตาราง และ ปุ่มบันทึกโพยทั้งหมด
def show_summary_footer():
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("🧹 ล้างตารางทั้งหมด", use_container_width=True):
            st.session_state.bills = []
            st.success("ล้างตารางเรียบร้อยแล้ว")

    with col2:
        if st.button("📥 บันทึกโพยทั้งหมด", use_container_width=True):
            if "bills" in st.session_state and st.session_state.bills:
                # ✅ เพิ่ม logic บันทึกข้อมูล หรือ export ได้ที่นี่
                st.success("บันทึกโพยทั้งหมดเรียบร้อยแล้ว ✅")
            else:
                st.warning("ยังไม่มีโพยในตารางให้บันทึก ❗")
