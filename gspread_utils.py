import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# ⚙️ ตั้งค่าชื่อ Google Sheet และ Worksheet
SHEET_NAME = "LottoBills"
WORKSHEET_BILLS = "โพยทั้งหมด"
WORKSHEET_SUMMARY = "สรุปยอดรวมเลข"

# ✅ เชื่อมต่อ Google Sheet ด้วย Service Account
def connect_google_sheet():
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    credentials = Credentials.from_service_account_file("credentials.json", scopes=scopes)
    gc = gspread.authorize(credentials)
    sh = gc.open(SHEET_NAME)
    return sh

# ✅ สร้าง Worksheet ถ้ายังไม่มี
def get_or_create_worksheet(sh, title, header_row):
    try:
        worksheet = sh.worksheet(title)
    except gspread.exceptions.WorksheetNotFound:
        worksheet = sh.add_worksheet(title=title, rows="1000", cols="10")
        worksheet.append_row(header_row)
    return worksheet

# ✅ ฟังก์ชันบันทึกโพยลง Google Sheet
def save_bills_to_gsheet(bills, memo, draw_date, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sh = connect_google_sheet()

    # เตรียม Worksheet โพยทั้งหมด
    header_bills = ["เวลาบันทึก", "งวดวันที่", "ประเภท", "เลข", "บน", "ล่าง", "โต๊ด", "บันทึกช่วยจำ"]
    worksheet_bills = get_or_create_worksheet(sh, WORKSHEET_BILLS, header_bills)

    rows_bills = []
    for bill in bills:
        rows_bills.append([
            timestamp,
            str(draw_date),
            bill.get("type", ""),
            bill.get("number", ""),
            bill.get("top", 0),
            bill.get("bottom", 0),
            bill.get("tod", 0),
            memo
        ])
    worksheet_bills.append_rows(rows_bills)

    # เตรียม Worksheet สรุปยอดรวมเลข
    summary = {}
    for bill in bills:
        num = bill["number"]
        if num not in summary:
            summary[num] = {"top": 0, "bottom": 0, "tod": 0}
        summary[num]["top"] += bill["top"]
        summary[num]["bottom"] += bill["bottom"]
        summary[num]["tod"] += bill.get("tod", 0)

    header_summary = ["เวลาบันทึก", "งวดวันที่", "เลข", "รวมบน", "รวมล่าง", "รวมโต๊ด", "บันทึกช่วยจำ"]
    worksheet_summary = get_or_create_worksheet(sh, WORKSHEET_SUMMARY, header_summary)

    rows_summary = []
    for num, val in summary.items():
        rows_summary.append([
            timestamp,
            str(draw_date),
            num,
            val["top"],
            val["bottom"],
            val["tod"],
            memo
        ])
    worksheet_summary.append_rows(rows_summary)
