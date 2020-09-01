import uuid
import config
import inference

import cv2
import numpy as np
from PIL import Image

import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to API"}


@app.post("/{style}")
def get_image(style: str, file: UploadFile = File(...)):
    image = np.array(Image.open(file.file))
    print(image.shape)
    model = config.STYLES[style]
    output, resized = inference.inference(model, image)
    name = f"/storage/{str(uuid.uuid4())}.jpg"
    cv2.imwrite(name, output)
    return {"name": name}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
