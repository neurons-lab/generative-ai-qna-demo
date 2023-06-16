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

video_file1 = open('media/alex_rotate.mp4', 'rb')
video_bytes1 = video_file1.read()
st.video(video_bytes1)

video_file2 = open('media/igor_rotate.mp4', 'rb')
video_bytes2 = video_file2.read()
st.video(video_bytes2)