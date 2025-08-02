import streamlit as st
from safe_utils import safe_rerun

def show_bill_table():
    st.subheader("🧾 ตารางบิลทั้งหมด")
    bills = st.session_state.get("bills", [])

    if not bills:
        st.info("ยังไม่มีบิลที่เพิ่มเข้ามา")
        return

    # รวมกลุ่ม
    grouped = {}
    for idx, bill in enumerate(bills):
        key = (bill["type"], bill["top"], bill["bottom"], bill.get("tod", 0))
        grouped.setdefault(key, []).append((idx, bill["number"]))

    for (bet_type, top, bottom, tod), entries in grouped.items():
        numbers = [num for _, num in entries]
        indices = [i for i, _ in entries]
        numbers_text = " ".join(numbers)

        cols = st.columns([4, 4, 1, 1])
        with cols[0]:
            st.markdown(f"**{bet_type}** บน:{top} ล่าง:{bottom} โต๊ด:{tod}")
        with cols[1]:
            st.markdown(numbers_text)
        with cols[2]:
            if st.button("✏️", key=f"edit_{indices[0]}"):
                index = indices[0]
                bill = bills[index]
                st.session_state.selected_numbers = [bill["number"]]
                st.session_state.input_text = bill["number"]
                st.session_state.price_top_value = bill["top"]
                st.session_state.price_bottom_value = bill["bottom"]
                st.session_state.price_tod_value = bill.get("tod", 0)
                st.session_state.edit_mode = True
                st.session_state.edit_index = index
                safe_rerun()
        with cols[3]:
            if st.button("🗑️", key=f"del_{indices[0]}"):
                for i in reversed(indices):
                    st.session_state.bills.pop(i)
                st.success("ลบบิลเรียบร้อย")
                safe_rerun()
