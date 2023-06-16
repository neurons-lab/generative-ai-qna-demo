#!/usr/bin/env python
import os
import streamlit as st

st.set_page_config(
    page_title="Neurons Lab Demo Website",
    # page_icon=":robot:",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

video_file3 = open('media/lilia_digital_avatar.mp4', 'rb')
video_bytes3 = video_file3.read()
st.video(video_bytes3)