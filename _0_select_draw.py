import streamlit as st
from datetime import datetime, timedelta

# กำหนดเวลา "ปิดรับแทง" ของแต่ละงวด เช่น 15:00 น.
CLOSE_TIME_HOUR = 15
CLOSE_TIME_MINUTE = 0

def get_time_remaining(closing_datetime):
    """คำนวณเวลาที่เหลือก่อนปิดรับแทง"""
    now = datetime.now()
    delta = closing_datetime - now
    if delta.total_seconds() <= 0:
        return "⛔ ปิดรับแทงแล้ว", True
    else:
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"⏳ เหลือเวลา: {hours:02d}:{minutes:02d}:{seconds:02d}", False

def select_draw():
    st.subheader("📅 เลือกงวดหวยที่จะแทง")

    # ให้เลือกวันที่ โดยค่าปริยายเป็นวันนี้
    today = datetime.today()
    default_draw_date = st.session_state.get("draw_date", today.date())

    draw_date = st.date_input(
        "เลือกวันที่งวดหวย",
        value=default_draw_date,
        min_value=today.date(),
        key="draw_date_input"
    )

    # คำนวณเวลาปิดรับแทงของวันนั้น
    close_time = datetime.combine(draw_date, datetime.min.time()) + timedelta(
        hours=CLOSE_TIME_HOUR, minutes=CLOSE_TIME_MINUTE
    )

    # แสดงเวลาปิดรับแทง
    st.write(f"🕒 ปิดรับแทงเวลา: {close_time.strftime('%H:%M น.')} ของวันที่ {draw_date.strftime('%d/%m/%Y')}")

    # แสดงเวลานับถอยหลัง
    time_left_str, is_closed = get_time_remaining(close_time)
    if is_closed:
        st.error(time_left_str)
    else:
        st.info(time_left_str)

    # เก็บค่า draw_date และ close_time ไว้ใน session_state
    st.session_state["draw_date"] = draw_date
    st.session_state["draw_close_time"] = close_time
    st.session_state["draw_closed"] = is_closed

# เรียกใช้ใน app.py แบบนี้:
# import _0_select_draw
# _0_select_draw.select_draw()
