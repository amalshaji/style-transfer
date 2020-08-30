import config
import inference
import base64
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
from PIL import Image
import numpy as np
import cv2
import uvicorn


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
    cv2.imwrite("output.jpg", output)
    return output.tolist()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
