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
y_img= 670
width = 290  
height = 110
image_path = "sskills.png"  
c.drawImage(image_path, x_img, y_img, width, height)
# bovenste lijn 
x3,y3=0,565
x4,y4=595,565
c.line(x3,y3,x4,y4)
#middelste lijn 
x1,y1=0,421
x2,y2=595,421
c.line (x1,y2,x2,y2)
# onderste lijn 
x5,y5 =279.5,310
x6,y6 = 595,310
c.line(x5,y5,x6,y6)

# normale tekst grote
c.setFont("Helvetica", 11)
# tekst klant
c.drawString(30, 750, "Adres: Europasingel 102693 GW Wervershoof")
c.drawString(30, 730, "Tel: 06-51944831")
c.drawString(30, 710, "E mail: SSkills@info.com")
#facatuur 
c.drawString(30,640, "INV-2025-001234")
c.drawString(145,640, "28 januari 2025")
c.drawString(250,640, "1 juni 2025")
#KVK BTW en bank
c.drawString(30,600, "KVK nummer")
c.drawString(145,600, "BTW nummer")
c.drawString(250,600, "Bank nummer") 
# uren bedrag btw
c.drawString(30,550, "Datum dienst geleverd - 28 januari-31januari")
c.drawString(30,530, "Dienst levering - fixen van software problemen")
c.drawString(270,550, "4 uren")
c.drawString(335,550, "€100")
c.drawString(420,550, "21%")
#klant
c.drawString(100,400, "Hans visser")
c.drawString(70,380, "Bloklandweg 4171 KA Herwijnen")
c.drawString(108,360, "12")
c.drawString(53,340, "+31 0345 - 12 34 56")
#Totaal +- btw
c.drawString(279.5,400, "Totaal exclusief btw (21%) ")
c.drawString(279.5,380, "Btw €")



#Dik gedrukte tekst 
c.setFont("Helvetica-Bold", 18)
#tekst facatuur
c.drawString(30,680, "Factuur")
c.setFont("Helvetica-Bold", 12)
c.drawString(30,660, "Factuur nummer")
c.drawString(145,660, "Factuur datum")
c.drawString(250,660, "verval datum") 
#KVK BTW en bank
c.drawString(30,620, "736493")
c.drawString(145,620, "83949484")
c.drawString(250,620, "93047372")
# uren bedrag btw
c.drawString(30,570, "Omschrijving")
c.drawString(270,570, "Uren")
c.drawString(335,570, "Bedrag")
c.drawString(420,570, "Btw")
#klant
c.drawString(30,400, "Klant naam:")
c.drawString(30,380, "Adres:")
c.drawString(30,360, "Huisnummer:")
c.drawString(30,340, "Tel:")
#Totaal +- btw
c.drawString(279.5,290, "Totaal inclusief btw (21%)") 




# Toon canvas
c.showPage()
# Sla canvas op
c.save()
print(f"Je PDF is opgeslagen in {file_name}")