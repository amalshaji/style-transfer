import io
import json
import base64
import streamlit as st
from PIL import Image
import numpy as np
import requests

STYLES = {
    "candy": "candy",
    "composition 6": "composition_vii",
    "feathers": "feathers",
    "la_muse": "la_muse",
    "mosaic": "mosaic",
    "starry night": "starry_night",
    "the scream": "the_scream",
    "the wave": "the_wave",
    "udnie": "udnie",
}

st.set_option("deprecation.showfileUploaderEncoding", False)

st.title("Style transfer web app")

image = st.file_uploader("Choose an image")

style = st.selectbox("Choose the style", [i for i in STYLES.keys()])

if st.button("Style Transfer"):
    if image is not None and style is not None:
        files = {"file": image.getvalue()}
        res = requests.post(f"http://backend:8080/{style}", files=files)
        img_path = res.json()
        image = Image.open(img_path.get("name"))
        st.image(image, width=500)
