import streamlit as st

def show_note_and_total():
    # คำนวณยอดรวมจาก session_state
    total_top = 0
    total_bottom = 0

    for bill in st.session_state.get("bills", []):
        top = bill.get("top", 0)
        bottom = bill.get("bottom", 0)
        total_top += top
        total_bottom += bottom

    total_amount = total_top + total_bottom

    # ✅ บรรทัดที่ 1: ยอดรวม
    st.markdown(
        f"""
        <div style='display: flex; align-items: center; font-size: 20px; font-weight: bold; margin-bottom: 20px;'>
            ยอดรวม: {total_amount} <span style='font-size: 16px; font-weight: normal;'>&nbsp;(บาท)</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ✅ บรรทัดที่ 2: บันทึกช่วยจำ (แนวเดียวกับ input)
    st.markdown(
        """
        <style>
        .memo-container {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .memo-label {
            min-width: 120px;
            font-weight: bold;
            font-size: 16px;
        }
        .memo-input input {
            height: 40px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("<div class='memo-label'>บันทึกช่วยจำ</div>", unsafe_allow_html=True)
    with col2:
        st.text_input(label="", key="memo", label_visibility="collapsed", placeholder="เช่น น้ำเต๋ม ของ VIP1")

