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
#middelste lijn 
x1,x2=0,421
y1,y2=595,421
c.line (x1,x2,y1,y2)

# Toon canvas
c.showPage()
# Sla canvas op
c.save()
print(f"Je PDF is opgeslagen in {file_name}")