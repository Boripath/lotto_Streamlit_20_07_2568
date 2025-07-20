import streamlit as st

# ตั้งค่าประเภทการแทง
bet_types = ["2 ตัว", "3 ตัว", "6 กลับ", "วิ่ง", "รูด", "19 ประตู"]

# ค่าเริ่มต้นถ้ายังไม่มีใน session
if "selected_bet_type" not in st.session_state:
    st.session_state.selected_bet_type = bet_types[0]

# ส่วนหัว
st.markdown("### 🎯 ประเภทการแทง")

# CSS สำหรับปุ่มที่ใช้ทั้งแสดงและเลือก
st.markdown("""
    <style>
    .bet-buttons-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 12px;
        margin-bottom: 20px;
    }

    .bet-button {
        border: 2px solid #1E90FF;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: 500;
        cursor: pointer;
        background-color: white;
        color: #1E90FF;
        transition: all 0.2s ease;
    }

    .bet-button.selected {
        background-color: #1E90FF;
        color: white;
    }

    .bet-button:hover {
        background-color: #e6f2ff;
    }
    </style>
""", unsafe_allow_html=True)

# แสดงปุ่มแบบ HTML + Form (1 บรรทัดเรียงกัน)
with st.form("bet_type_form", clear_on_submit=True):
    # สร้างปุ่มแบบ HTML
    html_buttons = "<div class='bet-buttons-container'>"
    for i, label in enumerate(bet_types):
        selected = "selected" if label == st.session_state.selected_bet_type else ""
        html_buttons += f"""
            <button name="bet_button" type="submit" value="{label}" class="bet-button {selected}">{label}</button>
        """
    html_buttons += "</div>"

    # แสดง HTML ปุ่ม
    st.markdown(html_buttons, unsafe_allow_html=True)

    # รับค่าการเลือก
    selected = st.form_submit_button()
    if selected:
        # อ่านค่าปุ่มจากฟอร์ม
        selected_type = st.experimental_get_query_params().get("bet_button", [None])[0]
        if selected_type in bet_types:
            st.session_state.selected_bet_type = selected_type

# แสดงผลที่เลือก
st.info(f"🔵 คุณเลือกประเภท: **{st.session_state.selected_bet_type}**")

# ปุ่มด้านล่าง
st.markdown("""
<div style='text-align:center; margin-top:10px;'>
    <button style='background-color:#1E90FF; color:white; border:none; padding:10px 20px; border-radius:8px; font-size:16px; font-weight:bold; cursor:pointer;'>
        ➕ ใส่เลขเบิ้ล/ตอง
    </button>
</div>
""", unsafe_allow_html=True)
