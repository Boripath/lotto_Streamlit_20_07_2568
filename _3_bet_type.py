import streamlit as st

def select_bet_type():
    st.markdown("### 🎯 ประเภทการแทง")

    # 🔹 ปุ่มเลือกประเภทการแทง
    bet_types = ["2 ตัว", "3 ตัว", "6 กลับ", "วิ่ง", "รูด", "19 ประตู"]

    if "selected_bet_type" not in st.session_state:
        st.session_state.selected_bet_type = "2 ตัว"

    cols = st.columns(len(bet_types))
    for i, label in enumerate(bet_types):
        with cols[i]:
            if st.button(label, use_container_width=True):
                st.session_state.selected_bet_type = label

    st.markdown(
        f"<p style='font-size:16px; color:#555;'>📌 เลือก: <b>{st.session_state.selected_bet_type}</b></p>",
        unsafe_allow_html=True
    )

    # 🔸 ปุ่มระบบช่วย
    st.markdown("---")
    st.markdown("#### 🧩 ระบบช่วย")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("➕ ใส่เลขเบิ้ล", use_container_width=True)
    with col2:
        st.button("➕ ใส่เลขโต๊ด", use_container_width=True)
    with col3:
        st.button("🔄 สลับเลข 6 กลับ", use_container_width=True)

    return st.session_state.selected_bet_type
