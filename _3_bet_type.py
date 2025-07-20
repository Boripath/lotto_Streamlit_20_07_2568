import streamlit as st

# กำหนดรายการประเภทการแทง
bet_types = ["2 ตัว", "3 ตัว", "6 กลับ", "วิ่ง", "รูด", "19 ประตู"]

# สร้างค่าเริ่มต้นถ้ายังไม่มีใน session
if "selected_bet_type" not in st.session_state:
    st.session_state.selected_bet_type = bet_types[0]

# แสดงหัวข้อ
st.markdown("### 🎯 ประเภทการแทง")

# CSS สำหรับปุ่ม
st.markdown("""
    <style>
    .bet-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 10px;
        margin-bottom: 20px;
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
        transition: all 0.2s ease;
    }
    .bet-button:hover {
        background-color: #e6f7ff;
    }
    .bet-button.selected {
        background-color: #00aaff;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# สร้างปุ่มในแถวเดียว
cols = st.columns(len(bet_types))
for i, label in enumerate(bet_types):
    is_selected = st.session_state.selected_bet_type == label
    btn_class = "bet-button selected" if is_selected else "bet-button"
    with cols[i]:
        if st.button(f"{label}", key=f"btn_{label}"):
            st.session_state.selected_bet_type = label
        st.markdown(f"<div class='{btn_class}'>{label}</div>", unsafe_allow_html=True)

# ✅ ปุ่มใส่เลขเบิ้ล/ตอง ด้านล่าง
st.markdown("""
    <div style='text-align:center; margin-top:10px;'>
        <button style='background-color:#00aaff; color:white; border:none; padding:10px 20px; border-radius:8px; font-size:16px; font-weight:bold; cursor:pointer;'>
            ➕ ใส่เลขเบิ้ล/ตอง
        </button>
    </div>
""", unsafe_allow_html=True)
