import streamlit as st

def select_pricerate():
    st.markdown("### 💸 อัตราจ่าย")
    rate = st.selectbox("เลือกอัตราจ่าย", ["บาทละ 70", "บาทละ 90"], index=1)
    st.markdown(f"<small style='color:gray;'>*อัตราจ่ายจะใช้กับทุกบิลที่ส่งในรอบนี้</small>", unsafe_allow_html=True)
    return rate  # ส่งออกให้ใช้ต่อได้
