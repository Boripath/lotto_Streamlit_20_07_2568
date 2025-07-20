import streamlit as st
from PIL import Image

# ❌ ถ้ายังไม่ติดตั้ง streamlit_extras ให้คอมเมนต์บรรทัดนี้ไว้ก่อน
# from streamlit_extras.stylable_container import stylable_container

def show_bill_table():
    # ✅ แสดงชื่อหวย + รูปธงแทน emoji
    st.markdown("""
        <div style='font-size:20px; font-weight:bold; margin-bottom:10px; display:flex; align-items:center; gap:10px;'>
            <img src="https://flagcdn.com/w40/th.png" width="28" style="vertical-align:middle;">
            หวยรัฐบาลไทย งวด วันศุกร์ 1/08/68
        </div>
    """, unsafe_allow_html=True)

    if "bills" not in st.session_state or not st.session_state.bills:
        st.info("ยังไม่มีบิลที่เพิ่มเข้ามา")
        return

    # ✅ รวมบิลที่เหมือนกันเข้าเป็นกลุ่ม
    grouped_bills = {}
    for bill in st.session_state.bills:
        key = (bill["type"], bill["top"], bill["bottom"])
        if key not in grouped_bills:
            grouped_bills[key] = []
        grouped_bills[key].append(bill["number"])

    # ✅ แสดงบิลแบบมีกรอบ
    for (bet_type, top, bottom), numbers in grouped_bills.items():
        with st.container():
            col1, col2, col3 = st.columns([2, 6, 1])
            with col1:
                st.markdown(f"""
                <div style='text-align:center; color:#3498db;'>
                    <b>{bet_type}</b><br>
                    <span style='color:#e74c3c;'>บน × ล่าง</span><br>
                    <b>{top} × {bottom}</b>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown(f"""
                <div style='font-size:18px; padding-top:10px;'>
                    {' '.join(numbers)}
                </div>
                """, unsafe_allow_html=True)
            with col3:
                col3a, col3b = st.columns([1, 1])
                with col3a:
                    st.button("✏️", key=f"edit_{bet_type}_{top}_{bottom}")
                with col3b:
                    st.button("🗑️", key=f"delete_{bet_type}_{top}_{bottom}")
