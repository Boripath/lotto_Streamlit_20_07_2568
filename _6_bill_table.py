import streamlit as st
from datetime import datetime

def show_bill_table():
    st.markdown(""" 
        <div style='display:flex; align-items:center; font-size:22px; font-weight:bold; border-bottom:2px solid #ccc; padding-bottom:10px; margin-bottom:20px;'>
            <img src='https://flagcdn.com/w40/th.png' style='margin-right:10px;'>
            หวยรัฐบาลไทย งวด {date}
        </div>
    """.format(
        date=st.session_state.get("draw_date", datetime.today().date()).strftime("%d/%m/%Y")
    ), unsafe_allow_html=True)

    if "bills" not in st.session_state or not st.session_state.bills:
        st.info("ยังไม่มีบิลที่เพิ่มเข้ามา")
        return

    # ✅ รวมบิลที่เหมือนกันเข้าเป็นกลุ่ม
    grouped_bills = {}
    for idx, bill in enumerate(st.session_state.bills):
        bet_type = bill.get("type", "")
        top = bill.get("top", 0)
        bottom = bill.get("bottom", 0)
        tod = bill.get("tod", 0)
        number = bill.get("number", "")

        key = (bet_type, top, bottom, tod)
        if key not in grouped_bills:
            grouped_bills[key] = []
        grouped_bills[key].append((idx, number))  # เก็บ index ด้วย

    # ✅ แสดงตาราง grouped แบบเดิม + ปุ่มต่อเลขแต่ละตัว
    for (bet_type, top, bottom, tod), items in grouped_bills.items():
        numbers_text = ""
        for idx, number in items:
            # ปุ่ม ✏️ / 🗑️ ในแต่ละเลข
            col_btns = (
                f"<button onclick=\"fetch('/?edit={idx}')\">✏️</button> "
                f"<button onclick=\"fetch('/?delete={idx}')\">🗑️</button>"
            )
            # ปรับให้ Streamlit ใช้จริง
            if st.button(f"✏️ แก้ไข {number}", key=f"edit_{idx}"):
                bill = st.session_state.bills[idx]
                st.session_state.selected_numbers = [bill["number"]]
                st.session_state.input_text = bill["number"]
                st.session_state.price_top_value = bill["top"]
                st.session_state.price_bottom_value = bill["bottom"]
                st.session_state.price_tod_value = bill.get("tod", 0)
                st.session_state.edit_mode = True
                st.session_state.edit_index = idx
                st.rerun()
            if st.button(f"🗑️ ลบ {number}", key=f"delete_{idx}"):
                st.session_state.bills.pop(idx)
                st.success(f"ลบบิล {number} แล้ว")
                st.rerun()

        # แสดงกล่องตาราง
        st.markdown(f"""
            <table style='width:100%; border-collapse:collapse; margin-bottom:10px;'>
                <tr style='border:1px solid #ccc;'>
                    <td style='width:20%; text-align:center; border:1px solid #ccc; padding:10px;'>
                        <div style='font-weight:bold; color:#3498db;'>{bet_type}</div>
                        <div style='font-size:14px; color:#e74c3c;'>บน × ล่าง × โต๊ด</div>
                        <div>{top} × {bottom} × {tod}</div>
                    </td>
                    <td style='width:80%; text-align:left; border:1px solid #ccc; padding:10px;'>
                        {" ".join([num for _, num in items])}
                    </td>
                </tr>
            </table>
        """, unsafe_allow_html=True)
