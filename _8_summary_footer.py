import streamlit as st
from datetime import datetime
from gspread_utils import save_bills_to_gsheet  # ต้องมีไฟล์นี้ในโปรเจกต์

def show_summary_footer():
    st.markdown("---")
    col1, col2 = st.columns([1, 1])

    # ปุ่มล้างตารางทั้งหมด
    with col1:
        if st.button("🧹 ล้างตารางทั้งหมด", use_container_width=True):
            st.session_state.bills = []
            st.session_state.input_text = ""
            st.session_state.selected_numbers = []
            st.session_state.price_top_value = 0
            st.session_state.price_bottom_value = 0
            st.session_state.price_tod_value = 0
            st.session_state.memo = ""
            st.success("✅ ล้างข้อมูลและตารางทั้งหมดเรียบร้อยแล้ว")
            st.experimental_rerun()

    # ปุ่มบันทึกโพยทั้งหมด
    with col2:
        if st.button("📥 บันทึกโพยทั้งหมด", use_container_width=True):
            if "bills" in st.session_state and st.session_state.bills:
                # ดึงข้อมูลที่ต้องใช้
                bills = st.session_state.bills
                memo = st.session_state.get("memo", "")
                draw_date = st.session_state.get("draw_date", datetime.today().date())
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # เรียกฟังก์ชันบันทึกข้อมูลลง Google Sheet
                try:
                    save_bills_to_gsheet(bills, memo, draw_date, timestamp)
                    st.success("✅ บันทึกโพยเรียบร้อยแล้ว")
                except Exception as e:
                    st.error(f"เกิดข้อผิดพลาดในการบันทึก: {e}")
            else:
                st.warning("⚠️ ยังไม่มีบิลในตารางให้บันทึก")
