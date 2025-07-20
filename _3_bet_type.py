import streamlit as st

def select_bet_type():
    st.markdown("### 🎯 ประเภทการแทง")

    bet_types = ["2 ตัว", "3 ตัว", "6 กลับ", "วิ่ง", "รูด", "19 ประตู"]
    helper_button = "➕ ใส่เลขเบิ้ล/ตอง"

    # ตั้งค่าเริ่มต้น
    if "selected_bet_type" not in st.session_state:
        st.session_state.selected_bet_type = "2 ตัว"

    # ✅ CSS ปรับแต่งปุ่ม
    st.markdown("""
        <style>
        .blue-button {
            border: 2px solid #1E90FF;
            border-radius: 8px;
            padding: 8px 16px;
            font-size: 16px;
            font-weight: 500;
            cursor: pointer;
            background-color: white;
            color: #1E90FF;
            width: 100%;
            text-align: center;
        }
        .blue-button.selected {
            background-color: #1E90FF !important;
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # ✅ ปุ่มแนวนอนด้วย st.columns
    cols = st.columns(len(bet_types))
    for i, label in enumerate(bet_types):
        is_selected = (label == st.session_state.selected_bet_type)
        button_label = f"<div class='blue-button {'selected' if is_selected else ''}'>{label}</div>"
        if cols[i].button(label, key=f"btn_{label}"):
            st.session_state.selected_bet_type = label
        cols[i].markdown(button_label, unsafe_allow_html=True)

    # ✅ ปุ่มระบบช่วย (บรรทัดที่ 2)
    st.markdown("---")
    st.markdown("<div class='blue-button'>➕ ใส่เลขเบิ้ล/ตอง</div>", unsafe_allow_html=True)

    return st.session_state.selected_bet_type
