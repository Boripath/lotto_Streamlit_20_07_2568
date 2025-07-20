import streamlit as st
import datetime

def render_header():
    # ✅ ใช้รูปภาพธงแทน Emoji
    flag_url = "https://upload.wikimedia.org/wikipedia/commons/a/a9/Flag_of_Thailand.svg"
    flag_html = f"<img src='{flag_url}' width='30' style='vertical-align: middle;'>"

    lottery_name = "หวยรัฐบาลไทย"
    draw_date_str = "วันศุกร์ 1/08/68"
    deadline_time = "15:00:00"

    full_date_text = "01/08/2568 " + deadline_time
    deadline_dt = datetime.datetime.strptime(full_date_text, "%d/%m/%Y %H:%M:%S")
    deadline_dt = deadline_dt.replace(year=deadline_dt.year - 543)

    now = datetime.datetime.now()
    remaining = deadline_dt - now

    if remaining.total_seconds() > 0:
        remaining_str = str(remaining).split(".")[0]
        countdown_html = f"<span style='color:red; font-size:18px;'>เหลือเวลาอีก {remaining_str}</span>"
    else:
        countdown_html = "<span style='color:gray; font-size:18px;'>ปิดรับโพยแล้ว</span>"

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
