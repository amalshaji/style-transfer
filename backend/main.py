import base64
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
from PIL import Image
import numpy as np

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to API"}


@app.post("/")
def get_image(file: UploadFile = File(...)):
    image = np.array(Image.open(file.file))
    return {"shape": image.shape}