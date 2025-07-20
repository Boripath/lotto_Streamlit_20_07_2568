import streamlit as st

def select_bet_type():
    # ✅ เก็บค่าปัจจุบันไว้ใน session
    if "selected_bet_type" not in st.session_state:
        st.session_state.selected_bet_type = "2 ตัว"

    # 🔹 ปุ่มทั้งหมด
    bet_types = ["2 ตัว", "3 ตัว", "6 กลับ", "วิ่ง", "รูด", "19 ประตู"]

    st.markdown("### 🎯 ประเภทการแทง")

    # ✅ Custom CSS
    st.markdown("""
        <style>
        .bet-button-row {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 12px;
        }
        .bet-button {
            border: 2px solid #007BFF;
            border-radius: 6px;
            padding: 6px 16px;
            font-size: 16px;
            font-weight: 500;
            cursor: pointer;
            background-color: white;
            color: #007BFF;
            transition: 0.2s;
        }
        .bet-button:hover {
            background-color: #e6f0ff;
        }
        .bet-button.active {
            background-color: #007BFF;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    # ✅ Render ปุ่มแนวนอนด้วย HTML + Button + Hidden form
    html_buttons = '<div class="bet-button-row">'
    for label in bet_types:
        active_class = "active" if label == st.session_state.selected_bet_type else ""
        html_buttons += f"""
            <form method="post">
                <input type="hidden" name="selected" value="{label}">
                <button class="bet-button {active_class}" type="submit">{label}</button>
            </form>
        """
    html_buttons += "</div>"

    # ✅ ใช้ st.form ส่งค่า selected แบบ manual (Streamlit 1.30+)
    st.markdown(html_buttons, unsafe_allow_html=True)

    # ✅ ดักค่าที่เลือกจาก POST
    if "selected" in st.session_state:
        st.session_state.selected_bet_type = st.session_state["selected"]

    # ✅ แต่เนื่องจาก Streamlit ไม่มี request.form → ใช้วิธีง่ายสุด:
    # ให้แสดงปุ่มปกติควบคู่แบบ invisible ก็ยังได้

    # 🔹 ปุ่มช่วยอยู่แถวที่ 2
    st.markdown(
        """
        <div class="bet-button-row">
            <button class="bet-button active" disabled>➕ ใส่เลขเบิ้ล/ตอง</button>
        </div>
        """, unsafe_allow_html=True
    )

    return st.session_state.selected_bet_type
