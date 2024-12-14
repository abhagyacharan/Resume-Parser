import pytesseract
from PIL import Image

# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path: str) -> str:
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

test1 = extract_text_from_image('D:/Github/Mental Health/resume-parser/files/abc_resume.png')
test2 = extract_text_from_image('D:/Github/Mental Health/resume-parser/files/anil.jpg')

print(test2)