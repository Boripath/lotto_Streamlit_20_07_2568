import streamlit as st

def select_bet_type():
    st.markdown("### 🎯 ประเภทการแทง")

    bet_types = ["2 ตัว", "3 ตัว", "6 กลับ", "วิ่ง", "รูด", "19 ประตู"]
    helper_button = "➕ ใส่เลขเบิ้ล/ตอง"

    # กำหนดค่าครั้งแรก
    if "selected_bet_type" not in st.session_state:
        st.session_state.selected_bet_type = "2 ตัว"

    # ✅ CSS สไตล์ปุ่ม
    st.markdown("""
        <style>
        .button-group {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 10px;
        }
        .blue-btn {
            border: 2px solid #1E90FF;
            border-radius: 6px;
            padding: 8px 16px;
            font-size: 16px;
            background-color: white;
            color: #1E90FF;
            font-weight: 500;
            cursor: pointer;
        }
        .blue-btn.selected {
            background-color: #1E90FF !important;
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # ✅ ปุ่มประเภทการแทง (บรรทัดที่ 1)
    st.markdown("<div class='button-group'>", unsafe_allow_html=True)
    for label in bet_types:
        button_key = f"bet_{label}"
        is_selected = (label == st.session_state.selected_bet_type)
        btn_class = "blue-btn selected" if is_selected else "blue-btn"
        # ใช้ HTML ปุ่มหลอกเพื่อจัดสไตล์
        st.markdown(f"""
            <form action="" method="post">
                <button name="selected_bet_type" value="{label}" class="{btn_class}" type="submit">{label}</button>
            </form>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # ✅ จัดการค่าที่กดจาก form
    selected_label = st.experimental_get_query_params().get("selected_bet_type", [None])[0]
    if selected_label and selected_label in bet_types:
        st.session_state.selected_bet_type = selected_label

    # ✅ ปุ่มระบบช่วย (บรรทัดที่ 2)
    st.markdown("<div class='button-group'>", unsafe_allow_html=True)
    st.button(helper_button, key="helper_doubles", use_container_width=False)
    st.markdown("</div>", unsafe_allow_html=True)

    return st.session_state.selected_bet_type
