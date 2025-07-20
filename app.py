import streamlit as st
from _1_header import render_header
from _2_pricerate import select_pricerate

st.set_page_config(page_title="โพยหวยออนไลน์", layout="centered")

# ✅ แสดงหัวเว็บ
render_header()

# ✅ เลือกอัตราจ่าย
rate = select_pricerate()
