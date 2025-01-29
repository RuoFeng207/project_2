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

# Toon canvas
c.showPage()
# Sla canvas op
c.save()
print(f"Je PDF is opgeslagen in {file_name}")