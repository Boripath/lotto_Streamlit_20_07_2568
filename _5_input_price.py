import streamlit as st

def input_prices():
    st.markdown("### 💰 ใส่ราคาสำหรับแต่ละเลข")

    if "selected_numbers" not in st.session_state:
        st.warning("ยังไม่มีเลข กรุณาใส่เลขก่อน")
        return {}

    if "price_data" not in st.session_state:
        st.session_state.price_data = {}

    for number in st.session_state.selected_numbers:
        col1, col2, col3 = st.columns([1, 2, 2])

        with col1:
            st.markdown(f"**{number}**")

        with col2:
            top_price = st.number_input(f"ราคาบน - {number}", min_value=0, value=st.session_state.price_data.get(number, {}).get("top", 0), key=f"top_{number}")
        
        with col3:
            bottom_price = st.number_input(f"ราคาล่าง - {number}", min_value=0, value=st.session_state.price_data.get(number, {}).get("bottom", 0), key=f"bottom_{number}")
        
        st.session_state.price_data[number] = {
            "top": top_price,
            "bottom": bottom_price
        }

    return st.session_state.price_data
