import streamlit as st

def select_bet_type():
    st.markdown("### 🎯 ประเภทการแทง")

    bet_types = ["2 ตัว", "3 ตัว", "6 กลับ", "วิ่ง", "รูด", "19 ประตู"]
    helper_button = "➕ ใส่เลขเบิ้ล/ตอง"

    if "selected_bet_type" not in st.session_state:
        st.session_state.selected_bet_type = "2 ตัว"

    # ✅ CSS Flexbox แนวนอน + ปรับปุ่ม
    st.markdown("""
        <style>
        .bet-row {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 16px;
        }
        .blue-button {
            border: 2px solid #1E90FF;
            border-radius: 8px;
            padding: 8px 16px;
            font-size: 16px;
            font-weight: 500;
            cursor: pointer;
            background-color: white;
            color: #1E90FF;
            min-width: 100px;
            text-align: center;
        }
        .blue-button.selected {
            background-color: #1E90FF !important;
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # ✅ แสดงปุ่มประเภทการแทง แนวนอน
    st.markdown("<div class='bet-row'>", unsafe_allow_html=True)
    for label in bet_types:
        is_selected = (label == st.session_state.selected_bet_type)
        button_html = f"""
            <form action="/" method="get">
                <button name="bet_type" value="{label}" type="submit" class="blue-button {'selected' if is_selected else ''}">{label}</button>
            </form>
        """
        st.markdown(button_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # ✅ อ่านค่าจาก query_params
    query_params = st.query_params
    if "bet_type" in query_params:
        st.session_state.selected_bet_type = query_params["bet_type"]

    # ✅ ปุ่มระบบช่วย (บรรทัดที่ 2)
    st.markdown("<div class='bet-row'><button class='blue-button selected'>{}</button></div>".format(helper_button), unsafe_allow_html=True)

    return st.session_state.selected_bet_type
