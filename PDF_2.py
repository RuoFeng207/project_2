# imports
import os, json 
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import *

file_name = "project_2.pdf"
doc_title = "project 2"
Title_pagina = "ScaleSkills"

# Maak canvas
c = canvas.Canvas(file_name, pagesize=A4)
width, height = A4
print(height,width)
# afbeelding
x_img= 280
y_img= 650
width = 300  
height = 120
image_path = "sskills.png"  
c.drawImage(image_path, x_img, y_img, width, height)
# bovenste lijn 
x3,y3=0,590
x4,y4=595,590
c.line(x3,y3,x4,y4)
#middelste lijn 
x1,y1=0,421
x2,y2=595,421
c.line (x1,y2,x2,y2)
# onderste lijn 
x5,y5 =279.5,210
x6,y6 = 595,210
c.line(x5,y5,x6,y6)


# tekst
c.drawString(30, 750, "Adres: Europasingel 102693 GW Wervershoof")
c.drawString(30, 730, "Tel: 06-51944831")
c.drawString(30, 710, "E mail: SSkills@info.com")

# Toon canvas
c.showPage()
# Sla canvas op
c.save()
print(f"Je PDF is opgeslagen in {file_name}")