import streamlit as st

def select_bet_type():
    st.markdown("### 🎯 ประเภทการแทง")

    # ตั้งค่าประเภทการแทงและปุ่มช่วย
    bet_types = ["2 ตัว", "3 ตัว", "6 กลับ", "วิ่ง", "รูด", "19 ประตู"]
    helper_buttons = ["➕ ใส่เลขเบิ้ล", "➕ ใส่เลขโต๊ด", "🔄 สลับเลข 6 กลับ"]

    # กำหนดค่าเริ่มต้น
    if "selected_bet_type" not in st.session_state:
        st.session_state.selected_bet_type = "2 ตัว"

    # CSS Style
    st.markdown("""
    <style>
    .button-row {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-bottom: 10px;
    }
    .custom-button {
        border: 2px solid #007BFF;
        border-radius: 6px;
        padding: 6px 16px;
        font-size: 16px;
        font-weight: 500;
        cursor: pointer;
        background-color: white;
        color: #007BFF;
    }
    .custom-button.selected {
        background-color: #007BFF;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    # 🔹 ปุ่มประเภทการแทง (แถวที่ 1)
    st.markdown("<div class='button-row'>", unsafe_allow_html=True)
    for label in bet_types:
        is_selected = (label == st.session_state.selected_bet_type)
        button_class = "custom-button selected" if is_selected else "custom-button"
        if st.button(label, key=f"bet_type_{label}"):
            st.session_state.selected_bet_type = label
        st.markdown(f"<button class='{button_class}' disabled>{label}</button>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 🔹 ปุ่มช่วย (แถวที่ 2)
    st.markdown("<div class='button-row'>", unsafe_allow_html=True)
    for label in helper_buttons:
        st.button(label, key=f"helper_{label}")
    st.markdown("</div>", unsafe_allow_html=True)

    return st.session_state.selected_bet_type
