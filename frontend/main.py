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

image = st.file_uploader("Upload your image...", type=["jpg", "png", "jpeg"])

style = st.selectbox("Choose the style", [i for i in STYLES.keys()])

if st.button("Style Transfer"):
    if image is not None and style is not None:
        shape = Image.open(image).shape
        files = {"file": image.getvalue()}
        res = requests.post(f"http://localhost:8000/{style}", files=files)
        image = np.frombuffer(res.content, dtype="float64")
        st.write(image.shape)
        image = np.reshape(image, (shape[0], shape[1]))
        st.write(image.shape)
