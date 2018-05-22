from PIL import Image
import pytesseract

im=Image.open("getCapchaImage.do.jpeg")
text = pytesseract.image_to_string(im,lang ='eng')

print(text)
