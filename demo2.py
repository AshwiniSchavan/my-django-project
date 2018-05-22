import mechanize
from PIL import Image
import pytesseract
import requests
import urllib
import cStringIO

path = "/home/ashwini/study/"
url = "https://ispeedtax.com/index.php/main/"

br = mechanize.Browser()
response = br.open(url + "login")
print(response.read())
image_responce = br.open(url + "captcha")
im = cStringIO.StringIO(image_responce.read())
img = Image.open(im)
path=img.save("image.png")
image_path = "/home/ashwini/study/image.png"
im=Image.open(image_path)
text = pytesseract.image_to_string(im,lang ='eng')
br.select_form(id="sky-formeee1")
form1 = br.form
form1["email"] = "ashvinich91@gmail.com"
form1["pwd"] = "####"
form1["captcha"] = text
print(form1)


'''
br = mechanize.Browser()
response = br.open(url + "login")
print(response.read())
br.select_form(id="sky-formeee1")
form1 = br.form
form1["email"] = "ashvinich91@gmail.com"
form1["pwd"] = "Ashvini@11"
print(form1)
# form1["captcha"] = text
'''
