from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os
from scripts.predict import predict_voice
from fastapi.staticfiles import StaticFiles 

app = FastAPI()

# Mount the static folder
app.mount("/static", StaticFiles(directory="static"), name="static")


from fastapi.responses import FileResponse

@app.get("/")
def home():
    return FileResponse("static/index.html")


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
