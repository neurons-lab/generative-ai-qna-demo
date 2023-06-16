#!/usr/bin/env python
import streamlit as st

# Set the page title and icon
st.set_page_config(
    page_title="Neurons Lab Demo Website",
    # page_icon=":robot:",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar class
class Home:
    '''Sidebar Personal Information Form'''
    def __init__(self, title, image):
        self.title = title
        self.image = image

    def render(self):
        '''Render'''
        col1, col2 = st.columns([1, 2])
        col1.image(self.image, width=250)
        col2.title(self.title)

        st.sidebar.success('Select Any Page to Start')
        st.sidebar.markdown('''
        **Contact Us:**\n
        info@neurons-lab.com\n
        +44 330 027 2146\n
        https://neurons-lab.com/\n
        ''')

# Sidebar widget
sidebar_widget = Home(
    title='Neurons Lab Demo Website',
    image='img/NeuronsLab.png'
)
sidebar_widget.render()

if __name__ == '__main__':
    pass
