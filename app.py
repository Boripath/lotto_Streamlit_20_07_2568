import streamlit as st
import datetime

# 📌 ตั้งค่าหวย
lottery_name = "หวยรัฐบาลไทย"
draw_date_str = "01/08/68"  # DD/MM/YY
draw_datetime = datetime.datetime.strptime("01/08/2568 15:00:00", "%d/%m/%Y %H:%M:%S")

# แปลงเป็น datetime ที่ Streamlit เข้าใจ (เนื่องจากปีพุทธศักราช)
draw_datetime = draw_datetime.replace(year=draw_datetime.year - 543)

# เวลาปัจจุบัน
now = datetime.datetime.now()
time_left = draw_datetime - now

# คำนวณเวลานับถอยหลัง
if time_left.total_seconds() > 0:
    time_str = str(time_left).split(".")[0]  # เอาเฉพาะ HH:MM:SS
    status = f"<span style='color:red; font-size:18px;'>⏰ เหลือเวลาอีก {time_str}</span>"
else:
    status = "<span style='color:gray; font-size:18px;'>🕒 ปิดรับโพยแล้ว</span>"

# 🎌 แถบบนสุด
st.markdown(
    f"""
    <div style='background-color:#f7f7f7; padding:15px; border-radius:10px; border:1px solid #ddd;'>
        <table style='width:100%;'>
            <tr>
                <td style='font-size:20px;'><span style='font-size:26px;'>🇹🇭</span> <b>{lottery_name}</b> งวด <b>{draw_date_str}</b></td>
                <td style='text-align:right;'>{status}</td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True
)
