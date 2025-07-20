import streamlit as st

st.markdown("""
    <style>
        .bet-container {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 20px;
        }
        .blue-button {
            padding: 0.5em 1em;
            border: 2px solid #0099ff;
            border-radius: 8px;
            background-color: white;
            color: #0099ff;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.2s, color 0.2s;
        }
        .blue-button:hover {
            background-color: #cceeff;
        }
        .blue-button.selected {
            background-color: #0099ff;
            color: white;
        }
        .helper-button {
            width: 100%;
            padding: 0.8em;
            border: 2px solid #0099ff;
            border-radius: 10px;
            background-color: white;
            color: #0099ff;
            font-weight: bold;
            margin-top: 15px;
            cursor: pointer;
            transition: background-color 0.2s, color 0.2s;
        }
        .helper-button:hover {
            background-color: #cceeff;
        }
        .helper-button.selected {
            background-color: #0099ff;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""<h4>🎯 ประเภทการแทง</h4>""", unsafe_allow_html=True)

bet_types = ["2 ตัว", "3 ตัว", "6 กลับ", "วิ่ง", "รูด", "19 ประตู"]

# ✅ ปุ่มเลือกประเภทการแทง
st.markdown("<div class='bet-container'>", unsafe_allow_html=True)
for label in bet_types:
    is_selected = st.session_state.get("selected_bet_type", "2 ตัว") == label
    button_html = f"""
        <form action="" method="get">
            <button name="bet_type" value="{label}" type="submit" class='blue-button {"selected" if is_selected else ""}'>{label}</button>
        </form>
    """
    st.markdown(button_html, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ✅ อ่านค่าจาก query param และเซ็ตค่า session state
if "bet_type" in st.query_params:
    st.session_state.selected_bet_type = st.query_params["bet_type"]

# ✅ ปุ่มระบบช่วย
helper_button_html = f"""
    <button class='helper-button'>
        <span style='font-size: 1.2em;'>➕ ใส่เลขเบิ้ล/ตอง</span>
    </button>
"""
st.markdown(helper_button_html, unsafe_allow_html=True)
