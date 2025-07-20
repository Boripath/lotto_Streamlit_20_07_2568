import streamlit as st

def select_bet_type():
    st.markdown("### 🎯 ประเภทการแทง")

    bet_types = ["2 ตัว", "3 ตัว", "6 กลับ", "วิ่ง", "รูด", "19 ประตู"]

    if "selected_bet_type" not in st.session_state:
        st.session_state.selected_bet_type = "2 ตัว"

    # ✅ CSS Styling
    st.markdown("""
        <style>
        .bet-container {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            justify-content: center;
            margin-bottom: 1rem;
        }
        .bet-button {
            border: 2px solid #00aaff;
            border-radius: 6px;
            padding: 8px 16px;
            font-size: 16px;
            font-weight: bold;
            color: #00aaff;
            background-color: white;
            cursor: pointer;
            text-align: center;
            transition: all 0.2s ease;
        }
        .bet-button:hover {
            background-color: #e6f7ff;
        }
        .bet-button.selected {
            background-color: #00aaff !important;
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # ✅ HTML ปุ่มทั้งหมดในแถวเดียว
    st.markdown('<div class="bet-container">', unsafe_allow_html=True)
    for label in bet_types:
        selected = (label == st.session_state.selected_bet_type)
        btn_class = "bet-button selected" if selected else "bet-button"
        if st.button(label, key=f"select_{label}"):
            st.session_state.selected_bet_type = label
        st.markdown(f"<div class='{btn_class}'>{label}</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ✅ ปุ่มใส่เลขเบิ้ล/ตอง
    st.markdown(
        """
        <div style='text-align:center;'>
            <button style='background-color:#00aaff; color:white; border:none; padding:10px 20px; border-radius:8px; font-size:16px; font-weight:bold; cursor:pointer;'>
                ➕ ใส่เลขเบิ้ล/ตอง
            </button>
        </div>
        """,
        unsafe_allow_html=True
    )

    return st.session_state.selected_bet_type
