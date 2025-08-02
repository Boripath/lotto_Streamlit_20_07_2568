import streamlit as st

def show_note_and_total():
    st.subheader("📝 บันทึกช่วยจำ และยอดรวมทั้งหมด")

    # คำนวณยอดรวมแยกแต่ละประเภท
    total_top = 0
    total_bottom = 0
    total_tod = 0

    for bill in st.session_state.get("bills", []):
        total_top += bill.get("top", 0)
        total_bottom += bill.get("bottom", 0)
        total_tod += bill.get("tod", 0)

    total_amount = total_top + total_bottom + total_tod

    # แสดงยอดรวม
    st.markdown(
        f"""
        <div style='font-size:18px; margin-bottom:10px;'>
            💵 รวมยอด: 
            <span style='color:#27ae60;'>บน {total_top} บาท</span> |
            <span style='color:#2980b9;'>ล่าง {total_bottom} บาท</span> |
            <span style='color:#8e44ad;'>โต๊ด {total_tod} บาท</span><br>
            <b>💰 รวมทั้งหมด: {total_amount} บาท</b>
        </div>
        """,
        unsafe_allow_html=True
    )

    # บันทึกช่วยจำ
    st.markdown("### 🗒️ บันทึกช่วยจำ")
    memo = st.text_input("เช่น ลูกค้า: ไทย1 / งวด 16/08/68", key="memo")

    # เก็บ memo ไว้ใน session_state
    st.session_state["memo"] = memo

    # คืนค่า memo และยอดรวมรวม
    return memo, total_amount
