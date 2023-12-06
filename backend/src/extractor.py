from PIL import Image
import pytesseract
import util

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract(file_path):
    # extracting text from the image
    img = Image.open(file_path)
    processed_image = util.preprocess_image(img)
    text = pytesseract.image_to_string(processed_image, lang='eng')

    return text




if __name__ == '__main__':
    data = extract('../resources/IMG-20231203-WA0012')
    print(data)