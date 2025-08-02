import streamlit as st
from streamlit.runtime.scriptrunner import RerunException
from streamlit.runtime.scriptrunner import get_script_run_ctx

def safe_rerun():
    ctx = get_script_run_ctx()
    if ctx:
        raise RerunException(ctx)
