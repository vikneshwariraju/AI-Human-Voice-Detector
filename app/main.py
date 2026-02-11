from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
import shutil
import os
from scripts.predict import predict_voice
from fastapi.staticfiles import StaticFiles 

app = FastAPI()

# Mount the static folder
app.mount("/", StaticFiles(directory="static", html=True), name="static")


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    temp_path = "temp.wav"

    # save uploaded audio
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # prediction
    result = predict_voice(temp_path)

    # remove temp file
    os.remove(temp_path)

    return {"prediction": result}
