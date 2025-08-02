import streamlit as st

def bet_type_selector():
    st.subheader("🎯 เลือกประเภทการแทง")

    # ค่าเริ่มต้นใน session_state
    if "selected_bet_type" not in st.session_state:
        st.session_state.selected_bet_type = "2 ตัว"
    if "double_mode" not in st.session_state:
        st.session_state.double_mode = False

    # ฟังก์ชัน: เปลี่ยนประเภทการแทง
    def set_bet_type(bet_type):
        st.session_state.selected_bet_type = bet_type

    # ฟังก์ชัน: toggle ใส่เลขเบิ้ล/ตอง
    def toggle_double():
        st.session_state.double_mode = not st.session_state.double_mode

    # ปุ่มเลือกประเภทการแทง (6 ปุ่ม)
    bet_types = ["2 ตัว", "3 ตัว", "6 กลับ", "วิ่ง", "รูด", "19 ประตู"]
    cols = st.columns(len(bet_types))
    for i, bet in enumerate(bet_types):
        with cols[i]:
            st.button(
                bet,
                on_click=set_bet_type,
                args=(bet,),
                use_container_width=True,
                type="primary" if st.session_state.selected_bet_type == bet else "secondary"
            )

    # คำอธิบายประเภทการแทง (optional)
    st.markdown(f"🔹 ประเภทที่เลือก: **{st.session_state.selected_bet_type}**")

    # ปุ่มใส่เลขเบิ้ล/ตอง
    st.markdown("---")
    double_btn_label = "➕ ใส่เลขเบิ้ล/ตอง" if not st.session_state.double_mode else "✅ เลือกใส่เลขเบิ้ล/ตองแล้ว"
    double_btn_type = "primary" if st.session_state.double_mode else "secondary"
    st.button(double_btn_label, on_click=toggle_double, use_container_width=True, type=double_btn_type)

    # แสดงสถานะเบิ้ล/ตอง (optional)
    if st.session_state.double_mode:
        st.info("ระบบจะเพิ่มเลขเบิ้ล เช่น 00, 11, 22, ... หรือเลขตอง เช่น 111, 222")

    # คืนค่า
    return st.session_state.selected_bet_type, st.session_state.double_mode
