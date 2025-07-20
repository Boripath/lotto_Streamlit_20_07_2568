import streamlit as st

def select_bet_type():
    # ค่าเริ่มต้น
    if "selected_bet_type" not in st.session_state:
        st.session_state.selected_bet_type = "2 ตัว"

    st.markdown("### 🎯 ประเภทการแทง")

    # 🔹 ประเภทการแทง
    bet_types = ["2 ตัว", "3 ตัว", "6 กลับ", "วิ่ง", "รูด", "19 ประตู"]

    # 🔹 ปุ่มระบบช่วย (บรรทัด 2)
    helper_buttons = ["➕ ใส่เลขเบิ้ล/ตอง"]

    # 🔷 STYLE ปุ่มทั้งหมด
    st.markdown("""
    <style>
    .bet-container {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-bottom: 10px;
    }
    .bet-button {
        border: 2px solid #007BFF;
        border-radius: 6px;
        padding: 6px 18px;
        font-size: 16px;
        font-weight: 500;
        color: #007BFF;
        background-color: white;
        cursor: pointer;
    }
    .bet-button.selected {
        background-color: #007BFF;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    # 🔹 แถวที่ 1: ประเภทการแทง
    st.markdown("<div class='bet-container'>", unsafe_allow_html=True)
    for label in bet_types:
        is_selected = (label == st.session_state.selected_bet_type)
        css_class = "bet-button selected" if is_selected else "bet-button"
        # แสดงปุ่ม HTML แทน st.button (เพราะต้องควบคุม CSS เอง)
        st.markdown(f"<button class='{css_class}' disabled>{label}</button>", unsafe_allow_html=True)
        # เพิ่มปุ่มจริง (แต่มองไม่เห็น) เพื่อจับ event
        if st.button(label, key=f"btn_{label}"):
            st.session_state.selected_bet_type = label
    st.markdown("</div>", unsafe_allow_html=True)

    # 🔹 แถวที่ 2: ปุ่มระบบช่วย
    st.markdown("<div class='bet-container'>", unsafe_allow_html=True)
    for label in helper_buttons:
        st.button(label, key=f"helper_{label}", use_container_width=False)
    st.markdown("</div>", unsafe_allow_html=True)

    return st.session_state.selected_bet_type
