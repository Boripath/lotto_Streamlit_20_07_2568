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
        bet_type = bill.get("type", "")
        top = bill.get("top", 0)
        bottom = bill.get("bottom", 0)
        number = bill.get("number", "")

        key = (bet_type, top, bottom)
        if key not in grouped_bills:
            grouped_bills[key] = []
        grouped_bills[key].append(number)

    # ✅ แสดงตารางแต่ละบิลแบบมีเส้น แบ่ง 4 คอลัมน์ ตามตัวอย่าง
    for (bet_type, top, bottom), numbers in grouped_bills.items():
        numbers_text = " ".join(numbers)
        st.markdown(f"""
            <table style='width:100%; border-collapse:collapse; margin-bottom:15px;'>
                <tr style='border:1px solid #ccc;'>
                    <td style='width:20%; text-align:center; vertical-align:middle; border:1px solid #ccc; padding:10px;'>
                        <div style='color:#3498db; font-weight:bold;'>{bet_type}</div>
                        <div style='color:#e74c3c;'>บน × ล่าง</div>
                        <div style='color:#3498db;'>{top} × {bottom}</div>
                    </td>
                    <td style='width:60%; text-align:left; vertical-align:middle; border:1px solid #ccc; padding:10px;'>
                        {numbers_text}
                    </td>
                    <td style='width:10%; text-align:center; vertical-align:middle; border:1px solid #ccc;'>
                        <button style='border:none; background-color:#fff; cursor:pointer;'>✏️</button>
                    </td>
                    <td style='width:10%; text-align:center; vertical-align:middle; border:1px solid #ccc;'>
                        <button style='border:none; background-color:#fff; cursor:pointer;'>🗑️</button>
                    </td>
                </tr>
            </table>
        """, unsafe_allow_html=True)

