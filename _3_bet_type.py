import streamlit as st

def select_bet_type():
    st.markdown("### 🎯 ประเภทการแทง")

    bet_types = ["2 ตัว", "3 ตัว", "6 กลับ", "วิ่ง", "รูด", "19 ประตู"]
    helper_button = "+ ใส่เลขเบิ้ล/ตอง"

    # ✅ กำหนดค่า default
    if "selected_bet_type" not in st.session_state:
        st.session_state.selected_bet_type = "2 ตัว"

    # ✅ สไตล์ปุ่มด้วย Streamlit Button + CSS
    button_css = """
        <style>
        .bet-btn-row {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-bottom: 10px;
        }
        .bet-btn-row button {
            border: 1.5px solid #007BFF;
            border-radius: 6px;
            padding: 6px 16px;
            font-size: 16px;
            font-weight: 500;
            background-color: white;
            color: #007BFF;
            cursor: pointer;
        }
        .bet-btn-row button.selected {
            background-color: #007BFF !important;
            color: white !important;
        }
        </style>
    """
    st.markdown(button_css, unsafe_allow_html=True)

    # ✅ ปุ่มประเภทการแทง
    st.markdown("<div class='bet-btn-row'>", unsafe_allow_html=True)
    for label in bet_types:
        is_selected = st.session_state.selected_bet_type == label
        btn_class = "selected" if is_selected else ""
        if st.button(label, key=f"bet_{label}", use_container_width=False):
            st.session_state.selected_bet_type = label
    st.markdown("</div>", unsafe_allow_html=True)

    # ✅ ปุ่มระบบช่วย 1 ปุ่ม
    st.markdown("<div class='bet-btn-row'>", unsafe_allow_html=True)
    st.button(helper_button, key="helper_doubles", use_container_width=False)
    st.markdown("</div>", unsafe_allow_html=True)

    return st.session_state.selected_bet_type
