#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
import pytesseract

im = Image.open('/Users/fanding/Desktop/fan.jpg')

result = pytesseract.image_to_string(im)

print(result)




import hashlib
m=hashlib.md5()
m.update('zhangkang'.encode('utf8'))
print(bin(m.hexdigest()))
