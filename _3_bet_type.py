import streamlit as st

def select_bet_type():
    st.markdown("### 🎯 ประเภทการแทง")

    bet_types = ["2 ตัว", "3 ตัว", "6 กลับ", "วิ่ง", "รูด", "19 ประตู"]
    help_buttons = ["➕ ใส่เลขเบิ้ล", "➕ ใส่เลขโต๊ด", "🔄 สลับเลข 6 กลับ"]

    if "selected_bet_type" not in st.session_state:
        st.session_state.selected_bet_type = "2 ตัว"

    # 🔹 สไตล์ปุ่ม
    def custom_button(label, is_selected):
        color = "#007BFF"  # ฟ้า
        bg = color if is_selected else "#FFFFFF"
        fg = "#FFFFFF" if is_selected else color
        border = f"1.5px solid {color}"
        style = f"""
            background-color: {bg};
            color: {fg};
            border: {border};
            border-radius: 6px;
            padding: 6px 16px;
            margin: 3px;
            font-size: 16px;
            font-weight: 500;
            cursor: pointer;
        """
        return st.markdown(
            f"<button style='{style}'>{label}</button>", unsafe_allow_html=True
        )

    # 🔹 ปุ่มประเภทการแทง
    st.markdown("<div style='display:flex; flex-wrap: wrap;'>", unsafe_allow_html=True)
    for label in bet_types:
        is_selected = (label == st.session_state.selected_bet_type)
        if st.button(label, key=f"bet_type_{label}", use_container_width=False):
            st.session_state.selected_bet_type = label
    st.markdown("</div>", unsafe_allow_html=True)

    # 🔹 ปุ่มระบบช่วย
    st.markdown("<div style='display:flex; flex-wrap: wrap;'>", unsafe_allow_html=True)
    for label in help_buttons:
        st.button(label, key=f"helper_{label}", use_container_width=False)
    st.markdown("</div>", unsafe_allow_html=True)

    return st.session_state.selected_bet_type
