import streamlit as st

# ----------------------------
# กำหนดค่าตั้งต้น
# ----------------------------
bet_types = ["2 ตัว", "3 ตัว", "6 กลับ", "วิ่ง", "รูด", "19 ประตู"]

# สร้างสถานะครั้งแรก
if "selected_bet_type" not in st.session_state:
    st.session_state.selected_bet_type = "2 ตัว"

# ----------------------------
# HTML และ CSS
# ----------------------------
st.markdown("""
<style>
.bet-container {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 0.75rem;
}
.bet-button {
    border: 2px solid #3399ff;
    color: #3399ff;
    background-color: white;
    padding: 0.5rem 1rem;
    font-size: 16px;
    border-radius: 8px;
    cursor: pointer;
    transition: 0.2s;
}
.bet-button:hover {
    background-color: #e6f2ff;
}
.bet-button.selected {
    background-color: #3399ff;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# JS ฟังค์ชันส่งค่าผ่าน query params
# ----------------------------
st.markdown("""
<script>
function selectBetType(type) {
    const url = new URL(window.location.href);
    url.searchParams.set("bet_type", type);
    window.location.href = url.toString();
}
</script>
""", unsafe_allow_html=True)

# ----------------------------
# ส่วนแสดงปุ่ม
# ----------------------------
st.markdown("<h4>🎯 ประเภทการแทง</h4>", unsafe_allow_html=True)

html_buttons = "<div class='bet-container'>"
for bt in bet_types:
    selected_class = "selected" if bt == st.session_state.selected_bet_type else ""
    html_buttons += f"""
    <button class='bet-button {selected_class}' onclick=\"selectBetType('{bt}')\">{bt}</button>
    """
html_buttons += "</div>"
st.markdown(html_buttons, unsafe_allow_html=True)

# ----------------------------
# อ่านค่าจาก URL แล้วอัปเดต session_state
# ----------------------------
bet_type_from_url = st.experimental_get_query_params().get("bet_type", [None])[0]
if bet_type_from_url and bet_type_from_url in bet_types:
    st.session_state.selected_bet_type = bet_type_from_url

# ----------------------------
# ปุ่มระบบช่วย
# ----------------------------
st.markdown("""
<div class='bet-container'>
    <button class='bet-button'>+ ใส่เลขเบิ้ล</button>
    <button class='bet-button'>+ ใส่เลขโต๊ด</button>
    <button class='bet-button'>+ สลับเลขแบบ 6 กลับ</button>
</div>
""", unsafe_allow_html=True)
