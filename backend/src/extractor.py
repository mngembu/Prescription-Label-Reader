from PIL import Image
import pytesseract
import outil

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract(file_path):
    # extracting text from the image
    img = Image.open(file_path)
    processed_image = outil.preprocess_image(img)
    text = pytesseract.image_to_string(processed_image, lang='eng')

    return text




if __name__ == '__main__':
    label_text = extract("resources/IMG-20231203-WA0010.jpg")
    print(label_text)