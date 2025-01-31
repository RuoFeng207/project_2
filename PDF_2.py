# imports
import factuur
import os, json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import *

file_name = "project_2.pdf"
doc_title = "project 2"
Title_pagina = "ScaleSkills"

# Maak canvas
c = canvas.Canvas(file_name, pagesize=A4)
f = factuur
width, height = A4
print(height, width)


# # Driehoek blauw
# c.setFillColor("#3877aa")  # Zet de vulkleur naar blauw (#3877aa)
# c.polygon([(0, 692), (297, 842), (0, 842)], fill=1)  # Teken en vul de blauwe driehoek

# # Driehoek geel
# c.setFillColor("#ffe464")  # Zet de vulkleur naar geel (#ffe464)
# c.polygon([(595, 150), (297, 0), (595, 0)], fill=1)  # Teken en vul de gele driehoek

# afbeelding
x_img = 280
y_img = 600  
width = 290
height = 110
image_path = os.path.dirname(os.path.abspath(__file__))+"\\sskills.png"
c.drawImage(image_path, x_img, y_img, width, height)

# Bovenste lijn
c.line(0, 505, 595, 505)

# Middelste lijn
c.line(0, 361, 595, 361)

# Onderste lijn
c.line(279.5, 250, 595, 250)

# Tekst bedrijf
c.setFont("Helvetica", 11)
c.drawString(30, 690, "Adres: Europasingel 102693 GW Wervershoof")
c.drawString(30, 670, "Tel: 06-51944831")
c.drawString(30, 650, "E mail: SSkills@info.com")


# Factuur
c.drawString(30, 580, "INV-2025-001234")
c.drawString(145, 580, "28 januari 2025")
c.drawString(250, 580, "1 juni 2025")

# KVK BTW en bank
c.drawString(30, 540, "736493")
c.drawString(145, 540, "83949484")
c.drawString(250, 540, "93047372")

# Uren bedrag btw
een = 490
if len(f.hoeveel) >= 1:
    c.drawString(30, 490, f"Geleverd product - {f.product1}")
    c.drawString(270, 490, f.aantal1)
    c.drawString(335, 490, f.prijszonder1)
    c.drawString(420, 490, f.btw1)
    if len(f.hoeveel) >= 2:
        c.drawString(30, 470, f"Geleverd product - {f.product2}")
        c.drawString(270, 470, f.aantal2)
        c.drawString(335, 470, f.prijszonder2)
        c.drawString(420, 470, f.btw2)
        if len(f.hoeveel) >= 3:
            c.drawString(30, 450, f"Geleverd product - {f.product3}")
            c.drawString(270, 450, f.aantal3)
            c.drawString(335, 450, f.prijszonder3)
            c.drawString(420, 450, f.btw3)
    

# Klant
c.drawString(100, 340, f.klant_naam )
c.drawString(70, 320, f.klant_adres)
c.drawString(90, 300, f.klant_postcode)
c.drawString(60, 280, f.klant_stad)
c.drawString(120, 260, f. ordernummer)


# Totaal +- btw
c.drawString(279.5, 340, f"Totaal exclusief btw € {f.prijzenTot}")
print(f.prijzenTot)
c.drawString(279.5, 320, "Btw €")
#btw prijzen
 #Dion
c.drawString(310, 320, "84")

# Inclusief btw
c.drawString(430, 230, "€")
#Dion
# c.drawString(440, 230, f.totale_prijs_incl_btw)

# Dik gedrukte tekst
c.setFont("Helvetica-Bold", 18)

# Tekst factuur
c.drawString(30, 620, "Factuur")
c.setFont("Helvetica-Bold", 12)
c.drawString(30, 600, "Factuur nummer")
c.drawString(145, 600, "Factuur datum")
c.drawString(250, 600, "Verval datum")
# KVK BTW en bank
c.drawString(30, 560, "KVK nummer")
c.drawString(145, 560, "BTW nummer")
c.drawString(250, 560, "Bank nummer")

# Uren bedrag btw
c.drawString(30, 510, "Omschrijving")
c.drawString(270, 510, "Aantal")
c.drawString(335, 510, "Bedrag")
c.drawString(420, 510, "Btw")

# Klant
c.drawString(30, 340, "Klant naam:")
c.drawString(30, 320, "Adres:")
c.drawString(30, 300, "Postcode:")
c.drawString(30, 280, "Stad:")
c.drawString(30, 260, "Order nummer:")

# Totaal +- btw
c.drawString(279.5, 230, "Totaal inclusief btw (21%)")

# Toon canvas
c.showPage()

# Sla canvas op
c.save()

print(f"Je PDF is opgeslagen in {file_name}")
