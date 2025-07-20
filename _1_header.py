import streamlit as st
import datetime

def render_header():
    # 🔸 ตั้งค่าข้อมูลหวย
    flag = "🇹🇭"
    lottery_name = "หวยรัฐบาลไทย"
    draw_date_str = "วันศุกร์ 1/08/68"
    deadline_time = "15:00:00"
    
    # 🔸 แปลงวันที่ (พ.ศ. → ค.ศ.)
    full_date_text = "01/08/2568 " + deadline_time
    deadline_dt = datetime.datetime.strptime(full_date_text, "%d/%m/%Y %H:%M:%S")
    deadline_dt = deadline_dt.replace(year=deadline_dt.year - 543)
    
    # 🔸 เวลาปัจจุบัน & คำนวณเวลาถอยหลัง
    now = datetime.datetime.now()
    remaining = deadline_dt - now

    if remaining.total_seconds() > 0:
        remaining_str = str(remaining).split(".")[0]
        countdown_html = f"<span style='color:red; font-size:18px;'>เหลือเวลาอีก {remaining_str}</span>"
    else:
        countdown_html = "<span style='color:gray; font-size:18px;'>ปิดรับโพยแล้ว</span>"

    # 🔸 แสดงแถบหัว
    st.markdown(
        f"""
        <div style='background-color:#fff; padding:10px 20px; border-radius:8px; border:1px solid #ccc; margin-bottom:10px;'>
            <table style='width:100%;'>
                <tr>
                    <td style='font-size:20px;'><span style='font-size:24px;'>{flag}</span> <b>{lottery_name}</b> งวด <b>{draw_date_str}</b></td>
                    <td style='text-align:right;'>{countdown_html}</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True
    )
