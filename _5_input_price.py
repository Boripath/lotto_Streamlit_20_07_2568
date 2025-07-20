import streamlit as st

def input_prices(selected_numbers, bet_type):
    if "bill_table" not in st.session_state:
        st.session_state.bill_table = []

    if not selected_numbers:
        st.info("กรุณากรอกเลขก่อน")
        return

    for number in selected_numbers:
        with st.container():
            col1, col2, col3, col4 = st.columns([1, 2, 2, 2])

            with col1:
                st.markdown(f"**{number}**")

            with col2:
                top_price = st.number_input(
                    label=f"บน {number}",
                    min_value=0,
                    step=1,
                    key=f"top_{number}",
                    label_visibility="collapsed",
                    placeholder="บน"
                )

            with col3:
                bottom_price = st.number_input(
                    label=f"ล่าง {number}",
                    min_value=0,
                    step=1,
                    key=f"bottom_{number}",
                    label_visibility="collapsed",
                    placeholder="ล่าง"
                )

            with col4:
                if st.button("➕ เพิ่มบิล", key=f"add_{number}"):
                    # เพิ่มบิลเข้า session_state
                    st.session_state.bill_table.append({
                        "bet_type": bet_type,
                        "number": number,
                        "top": top_price,
                        "bottom": bottom_price
                    })
                    # ล้างค่า input หลังเพิ่ม
                    st.session_state[f"top_{number}"] = 0
                    st.session_state[f"bottom_{number}"] = 0
                    st.success(f"เพิ่ม {number} สำเร็จแล้ว", icon="✅")
