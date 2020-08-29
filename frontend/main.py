import io
import json
import base64
import streamlit as st
from PIL import Image
import numpy as np
import requests

st.set_option("deprecation.showfileUploaderEncoding", False)

st.title("Style transfer web app")

# style = st.sidebar.selectbox("choose a style", ["one", "two", "three"], key="style")

# process = st.sidebar.button("Apply")

# if process:
#     st.write(style)


image = st.file_uploader("Choose an image")

if image is not None:
    files = {"file": image.getvalue()}
    res = requests.post("http://backend:8000/", files=files)
    st.write(res.json())