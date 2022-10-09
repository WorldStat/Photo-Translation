# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:58:16 2021

@author: Dmytro
"""

import cv2

from PIL import Image

import pytesseract
from google_trans_new import google_translator



#Converting 1st page of PDF to PNG
#pages = convert_from_path('D:\Spyder projects\Recognizer\DERS 3.pdf',500,first_page=1, last_page=1)
#for page in pages:
   # page.save('out.png', 'PNG')


# Reading PNG, converting color, showing it 
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
#tessdata_dir_config = "C:\Program Files\Tesseract-OCR\tessdata\\"
img = cv2.imread('p2C1.jpg')
image = Image.open('p2C1.jpg')
print(image.size)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(img, lang='tur')
text = text.replace("\n", " ")
text = text.split()

translator = google_translator() 

t_text = []
for w in text:
    result = translator.translate(w, lang_src='tr', lang_tgt='en')
    t_text.append(result)



count = 0
was_moved = 0
boxes = pytesseract.image_to_data(img)
for x, b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        #print(b)
        if len(b) == 12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            #cv2.rectangle(img, (x,y), (w+x,h+y), (0,0,255), 3)
            if len(t_text[count]) >= 6:
                if was_moved == 0:
                    x += 34
                    was_moved = 1
                else:
                    was_moved = 0
            cv2.putText(img, t_text[count], (x,y), cv2.FONT_HERSHEY_COMPLEX, 1.5, (50,50,255),2)
            count = count+1



cv2.imwrite('Result-en.jpeg', img)
cv2.waitKey(0)
        
        

































