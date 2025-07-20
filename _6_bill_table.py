import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# ✅ ฟังก์ชันแสดงหัวตารางพร้อมธงชาติ

def show_bill_table():
    st.markdown("""
        <div style='display:flex; align-items:center; font-size:22px; font-weight:bold; border-bottom:2px solid #ccc; padding-bottom:10px; margin-bottom:20px;'>
            <img src='https://flagcdn.com/w40/th.png' style='margin-right:10px;'>
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

    # ✅ แสดงตารางแต่ละบิลแบบมีเส้น และจัดให้สวยงาม
    for (bet_type, top, bottom), numbers in grouped_bills.items():
        st.markdown("""
            <div style='border:1px solid #ccc; border-radius:8px; padding:15px; margin-bottom:15px; display:flex; justify-content:space-between; align-items:center;'>
                <div style='display:flex; flex-direction:column;'>
                    <div style='color:#3498db; font-weight:bold;'>{}</div>
                    <div style='color:#e74c3c;'>บน × ล่าง</div>
                    <div style='color:#3498db;'>{} × {}</div>
                </div>
                <div style='flex-grow:1; text-align:left; padding:0 20px; font-size:18px;'>
                    {}
                </div>
                <div style='display:flex; gap:10px;'>
                    <button style='border:none; background-color:#fff; cursor:pointer;'>✏️</button>
                    <button style='border:none; background-color:#fff; cursor:pointer;'>🗑️</button>
                </div>
            </div>
        """.format(bet_type, top, bottom, " ".join(numbers)), unsafe_allow_html=True)
