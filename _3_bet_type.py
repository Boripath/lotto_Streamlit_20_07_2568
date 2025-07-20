import streamlit as st

def select_bet_type():
    st.markdown("### 🎯 ประเภทการแทง")

    bet_types = ["2 ตัว", "3 ตัว", "6 กลับ", "วิ่ง", "รูด", "19 ประตู"]
    helper_button = "➕ ใส่เลขเบิ้ล/ตอง"

    # ตั้งค่าเริ่มต้น
    if "selected_bet_type" not in st.session_state:
        st.session_state.selected_bet_type = "2 ตัว"

    # ✅ CSS Styling
    st.markdown("""
        <style>
        .bet-button {
            border: 2px solid #00aaff;
            border-radius: 6px;
            padding: 8px;
            margin: 4px;
            font-size: 16px;
            font-weight: bold;
            color: #00aaff;
            background-color: white;
            width: 100%;
            text-align: center;
        }
        .bet-button.selected {
            background-color: #00aaff !important;
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # ✅ แนวนอน: 6 ปุ่มใน 6 columns
    cols = st.columns(len(bet_types))
    for i, label in enumerate(bet_types):
        is_selected = (label == st.session_state.selected_bet_type)
        btn_class = "bet-button selected" if is_selected else "bet-button"
        btn_html = f"<div class='{btn_class}'>{label}</div>"

        # ดักคลิก
        if cols[i].button(label, key=f"btn_{label}"):
            st.session_state.selected_bet_type = label

        # ปรับ CSS overlay หลังจากคลิก
        cols[i].markdown(btn_html, unsafe_allow_html=True)

    # ✅ ปุ่มระบบช่วย
    st.markdown("")
    st.markdown("<div class='bet-button selected'>➕ ใส่เลขเบิ้ล/ตอง</div>", unsafe_allow_html=True)

    return st.session_state.selected_bet_type
