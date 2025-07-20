import streamlit as st
import datetime

# 📌 ตั้งค่าหวย
lottery_name = "หวยฮานอย พิเศษ"
flag_emoji = "🇻🇳"
draw_date_str = "20/07/68"  # งวดแบบไทย
draw_datetime = datetime.datetime.strptime("20/07/2568 15:00:00", "%d/%m/%Y %H:%M:%S")
draw_datetime = draw_datetime.replace(year=draw_datetime.year - 543)  # ปี พ.ศ. → ค.ศ.

# เวลาปัจจุบันและเวลานับถอยหลัง
now = datetime.datetime.now()
time_left = draw_datetime - now
if time_left.total_seconds() > 0:
    time_str = str(time_left).split(".")[0]
    status_html = f"<span style='color:#e74c3c; font-size:18px;'>เหลือเวลาอีก {time_str}</span>"
else:
    status_html = "<span style='color:gray; font-size:18px;'>ปิดรับโพยแล้ว</span>"

# 🧾 ส่วนหัว
st.markdown(
    f"""
    <div style='background-color:#fdfdfd; padding:10px 20px; border-radius:8px; border:1px solid #ccc; margin-bottom:10px;'>
        <table style='width:100%;'>
            <tr>
                <td style='font-size:20px;'><span style='font-size:24px;'>{flag_emoji}</span> <b>{lottery_name}</b> งวด <b>{draw_date_str}</b></td>
                <td style='text-align:right;'>{status_html}</td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True
)

# 🔢 อัตราจ่าย
st.markdown("### 💸 อัตราจ่าย")
rate = st.selectbox("เลือกอัตราจ่าย", ["บาทละ 70", "บาทละ 90"], index=1)
st.markdown(f"<small style='color:gray;'>*อัตราจ่ายจะใช้กับทุกบิลที่ส่งในรอบนี้</small>", unsafe_allow_html=True)
