import streamlit as st
import pandas as pd

# ตัวอย่างข้อมูลหวย
LOTTERY_FLAG = "🇹🇭"
LOTTERY_NAME = "หวยรัฐบาลไทย"
LOTTERY_ROUND = "วันศุกร์ 1/08/68"


def show_bill_table():
    st.markdown(
        f"""
        <div style='font-size:20px; font-weight:bold; margin-bottom:10px;'>
            {LOTTERY_FLAG} {LOTTERY_NAME} งวด {LOTTERY_ROUND}
        </div>
        """,
        unsafe_allow_html=True
    )

    if "bills" not in st.session_state or not st.session_state.bills:
        st.info("ยังไม่มีบิลที่เพิ่มเข้ามา")
        return

    # รวมบิลที่ซ้ำกัน (ประเภท, ราคาบน, ราคาล่าง) เข้าเป็นกลุ่มเดียวกัน
    df = pd.DataFrame(st.session_state.bills)
    grouped = df.groupby(["type", "top", "bottom"], as_index=False).agg({"number": lambda x: ' '.join(x)})

    # แสดงเป็นตารางพร้อมปุ่ม
    for i, row in grouped.iterrows():
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 3, 1])
        col1.markdown(f"<div style='padding-top:8px'><b>{row['type']}</b></div>", unsafe_allow_html=True)
        col2.markdown(f"<div style='padding-top:8px'>💰 {row['top']}</div>", unsafe_allow_html=True)
        col3.markdown(f"<div style='padding-top:8px'>💲 {row['bottom']}</div>", unsafe_allow_html=True)
        col4.markdown(f"<div style='padding-top:8px'>{row['number']}</div>", unsafe_allow_html=True)

        if col5.button("\U0001F58A\ufe0f", key=f"edit_{i}"):
            st.warning("🔄 ฟีเจอร์แก้ไขกำลังพัฒนา")
        if col5.button("\u274c", key=f"delete_{i}"):
            # ลบบิลที่อยู่ในกลุ่มนี้ทั้งหมดออกจาก session_state
            st.session_state.bills = [bill for bill in st.session_state.bills
                                      if not (bill['type'] == row['type'] and bill['top'] == row['top']
                                              and bill['bottom'] == row['bottom'] and bill['number'] in row['number'].split())]
            st.rerun()


if __name__ == "__main__":
    show_bill_table()
