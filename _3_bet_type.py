import streamlit as st

def bet_type_selector():
    st.markdown("### ")

    # ✅ เก็บประเภทที่เลือกไว้ใน session_state
    if "selected_bet_type" not in st.session_state:
        st.session_state.selected_bet_type = "2 ตัว"

    if "double_mode" not in st.session_state:
        st.session_state.double_mode = False

    # ✅ ฟังก์ชันเลือกประเภทการแทง
    def set_bet_type(bet_type):
        st.session_state.selected_bet_type = bet_type

    # ✅ ฟังก์ชัน toggle เลขเบิ้ล/ตอง
    def toggle_double():
        st.session_state.double_mode = not st.session_state.double_mode

    # ✅ ปุ่มประเภทการแทง
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.button("2 ตัว", on_click=set_bet_type, args=("2 ตัว",), use_container_width=True,
                  type="primary" if st.session_state.selected_bet_type == "2 ตัว" else "secondary")
    with col2:
        st.button("3 ตัว", on_click=set_bet_type, args=("3 ตัว",), use_container_width=True,
                  type="primary" if st.session_state.selected_bet_type == "3 ตัว" else "secondary")
    with col3:
        st.button("6 กลับ", on_click=set_bet_type, args=("6 กลับ",), use_container_width=True,
                  type="primary" if st.session_state.selected_bet_type == "6 กลับ" else "secondary")
    with col4:
        st.button("วิ่ง", on_click=set_bet_type, args=("วิ่ง",), use_container_width=True,
                  type="primary" if st.session_state.selected_bet_type == "วิ่ง" else "secondary")
    with col5:
        st.button("รูด", on_click=set_bet_type, args=("รูด",), use_container_width=True,
                  type="primary" if st.session_state.selected_bet_type == "รูด" else "secondary")
    with col6:
        st.button("19 ประตู", on_click=set_bet_type, args=("19 ประตู",), use_container_width=True,
                  type="primary" if st.session_state.selected_bet_type == "19 ประตู" else "secondary")

    # ✅ ปุ่ม +ใส่เลขเบิ้ล/ตอง
    st.markdown("---")
    double_btn_class = "primary" if st.session_state.double_mode else "secondary"
    st.button("➕ ใส่เลขเบิ้ล/ตอง", on_click=toggle_double, use_container_width=True, type=double_btn_class)

    # ✅ คืนค่าไปใช้งานต่อ
    return st.session_state.selected_bet_type, st.session_state.double_mode
