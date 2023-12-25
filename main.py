from src.loggings import logger
from fastapi import FastAPI, Form, UploadFile, File
import uvicorn
from src.extractor import extract
import uuid
import os
import sys
from src.exception import CustomException
from PIL import Image

app = FastAPI()


@app.post("/speech_from_doc")
def speech_from_doc(file: UploadFile):     # UploadFile (specific to FastAPI) is the data type of the file. (...) means not passing any value

    contents = file.file.read()

    # save the temporary image file from Postman to a temporary location for the extractor to use
    file_path = "uploads/" + str(uuid.uuid4()) + ".jpg"

    with open(file_path, "wb") as f:
        f.write(contents)

    try:
        data = extract(file_path)
    except Exception as e:
        #data = {'error': str(e)}
        raise CustomException(e, sys)

    # delete the temporary image file after each run
    if os.path.exists(file_path):
        os.remove(file_path)

    logger.info("Voice message created and saved to file")

    return data


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

