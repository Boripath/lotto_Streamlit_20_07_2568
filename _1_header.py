import streamlit as st
from datetime import datetime, timedelta

def render_header():
    # ✅ ธงชาติไทย
    flag_url = "https://upload.wikimedia.org/wikipedia/commons/a/a9/Flag_of_Thailand.svg"
    flag_html = f"<img src='{flag_url}' width='30' style='vertical-align: middle;'>"

    # ✅ ใช้ชื่อหวย และวันงวดจาก session_state (ตั้งค่าจาก _0_select_draw.py)
    lottery_name = "หวยรัฐบาลไทย"
    draw_date = st.session_state.get("draw_date", datetime.today().date())
    close_time = st.session_state.get("draw_close_time", datetime.combine(draw_date, datetime.min.time()) + timedelta(hours=15))
    is_closed = st.session_state.get("draw_closed", False)

    # แปลงวันเป็นภาษาไทย
    weekday_thai = ["วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์", "วันอาทิตย์"]
    draw_date_th = draw_date.strftime("%d/%m/%Y")
    weekday_str = weekday_thai[draw_date.weekday()]
    draw_date_str = f"{weekday_str} {draw_date_th}"

    # เวลานับถอยหลัง
    now = datetime.now()
    remaining = close_time - now
    if remaining.total_seconds() > 0:
        days = remaining.days
        hours, rem = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(rem, 60)
        time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
        remaining_str = f"{days} วัน {time_str}"
        countdown_html = f"<span style='color:red; font-size:18px;'>เหลือเวลาอีก {remaining_str}</span>"
    else:
        countdown_html = "<span style='color:gray; font-size:18px;'>⛔ ปิดรับโพยแล้ว</span>"

    # ✅ แสดงหัวเว็บสวย ๆ
    st.markdown(
        f"""
        <div style='background-color:#fff; padding:10px 20px; border-radius:8px; border:1px solid #ccc; margin-bottom:10px;'>
            <table style='width:100%; vertical-align:middle;'>
                <tr>
                    <td style='font-size:20px;'>{flag_html} <b>{lottery_name}</b> งวด <b>{draw_date_str}</b></td>
                    <td style='text-align:right;'>{countdown_html}</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True
    )
