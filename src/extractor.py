from PIL import Image
import pytesseract
import src.outil

from src.loggings import logger
from src.parser_prescription import PrescriptionParser

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract(file_path):
    # extracting text from the image
    if file_path.endswith('.jpg'):
        img = Image.open(file_path)
        processed_image = src.outil.preprocess_image(img)
        text = pytesseract.image_to_string(processed_image, lang='eng')

        logger.info("Text message created")

    # extracting fields from the text and converting to speech  
        output_voice = PrescriptionParser(text).parse()

        logger.info("Voice message created and saved to file")

    else:
        raise Exception(f"Invalid file format")

    return output_voice


#if __name__ == '__main__':
    #extract("../resources/IMG-20231203-WA0010.jpg")
    