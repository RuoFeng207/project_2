# imports
import factuur_2 
import os, json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import *

file_name = "project_3.pdf"
doc_title = "project 3"
Title_pagina = "ScaleSkills"

# Maak canvas
c = canvas.Canvas(file_name, pagesize=A4)
f = factuur_2
width, height = A4
print(height, width)


# achtergrond
x_img2 = 0
y_img2 = 0  
width2 = 595
height2 = 842
image_path2 =  os.path.dirname(os.path.abspath(__file__))+"\\project_2pdf.png"
c.drawImage(image_path2, x_img2, y_img2, width2, height2)

# afbeelding logo
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
c.drawString(30, 650, "E mail: ScaleSkills@info.com")


# Factuur
c.drawString(30, 580, "INV-2025-001234")
c.drawString(145, 580, f.orderdatum)
c.drawString(250, 580, f.betaaltermijn)

# KVK BTW en bank
c.drawString(30, 540, f.kvk_nummer)
c.drawString(145, 540, "83949484")
c.drawString(250, 540, "93047372")

# Uren bedrag btw
c.drawString(30, 490, f"Product naam - {f.productnaam}")
c.drawString(280, 490, str(f.aantal))
c.drawString(345, 490, str(f.prijs_per_stuk))
c.drawString(430, 490, str(f"{f.btw_percentage}%"))

# Klant
c.drawString(100, 340, f.naam_klant )
c.drawString(70, 320, f.aderes_klant)
c.drawString(90, 300, f.postcode_klant)
c.drawString(60, 280, f.stad_klant)
c.drawString(120, 260, f. ordernummer)


# Totaal +- btw
c.drawString(279.5, 340, f"Totaal exclusief btw € {f.prijs_excl_btw:.2f}")
c.drawString(279.5, 320, "Btw €")
#btw prijzen

c.drawString(310, 320, f"{f.btw:.2f}")

# Inclusief btw
c.drawString(430, 230, "€")
c.drawString(430, 230, f"€ {f.prijs_incl_btw}")

# Dik gedrukte tekst
c.setFont("Helvetica-Bold", 18)

# Tekst factuur
c.drawString(30, 620, "Factuur")
c.setFont("Helvetica-Bold", 12)
c.drawString(30, 600, "Factuur nummer")
c.drawString(145, 600, "Factuur datum")
c.drawString(250, 600, "Betaaltermijn")
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
c.drawString(279.5, 230, f"Totaal inclusief btw ({f.btw_percentage}%)")

# Toon canvas
c.showPage()

# Sla canvas op
c.save()

print(f"Je PDF is opgeslagen in {file_name}")