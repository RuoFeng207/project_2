# imports
import os
import json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Haal de JSON-bestanden op uit de map
json_location = os.path.join(os.path.dirname(__file__), "JSON_ORDER")
json_bestanden = [bestandsnaam for bestandsnaam in os.listdir(json_location) if bestandsnaam.endswith(".json")]

# Verplaats map
output_folder = os.path.join(os.path.dirname(__file__), "JSON_PROCESSED")  # Doelmap voor verplaatsen
# Controleer of de map bestaat, anders maak deze aan
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

getal = 1

for bestandnaam in json_bestanden:
    file_name = f"bestand_{getal}.pdf"
    doc_title = "project 2"
    Title_pagina = "ScaleSkills"

    # Maak canvas
    c = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4
    print(height, width)

    # Achtergrond
    x_img2 = 0
    y_img2 = 0  
    width2 = 595
    height2 = 842
    image_path2 = os.path.dirname(os.path.abspath(__file__)) + "\\project_2pdf.png"
    c.drawImage(image_path2, x_img2, y_img2, width2, height2)

    # Logo afbeelding
    x_img = 280
    y_img = 600  
    width = 290
    height = 110
    image_path = os.path.dirname(os.path.abspath(__file__)) + "\\sskills.png"
    c.drawImage(image_path, x_img, y_img, width, height)

    # Bovenste lijn
    c.line(0, 505, 595, 505)
    # Middelste lijn
    c.line(0, 361, 595, 361) 
    # Onderste lijn
    c.line(279.5, 250, 595, 250) 

    # Tekst bedrijfsinformatie
    c.setFont("Helvetica", 11)
    c.drawString(30, 690, "Adres: Europasingel 102693 GW Wervershoof")
    c.drawString(30, 670, "Tel: 06-51944831")
    c.drawString(30, 650, "E mail: ScaleSkills@info.com")

    # Laad de JSON-data uit het bestand
    bestandspad = os.path.join(json_location, bestandnaam)
    with open(bestandspad, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Haal de benodigde gegevens uit het bestand
    order = data.get("order", {})
    ordernummer = order.get("ordernummer")
    orderdatum = order.get("orderdatum")
    betaaltermijn = order.get("betaaltermijn")
    klant = order.get("klant", {})
    naam_klant = klant.get("naam")
    aderes_klant = klant.get("adres")
    postcode_klant = klant.get("postcode")
    stad_klant = klant.get("stad")
    kvk_nummer = klant.get("KVK-nummer")
    producten = order.get("producten", [])

    # Factuurgegevens
    c.drawString(30, 580, f"INV-2025-001234")  # Factuurnummer
    c.drawString(145, 580, orderdatum)  # Factuurdatum
    c.drawString(250, 580, betaaltermijn)  # Betaaltermijn

    # KVK BTW en bankgegevens
    c.drawString(30, 540, kvk_nummer)
    c.drawString(145, 540, "83949484")
    c.drawString(250, 540, "93047372")

    # Producten, aantal, prijs, btw
    y_cordinaat = 490
    totaal_prijs_incl_btw = 0
    totaal_prijs_excl_btw = 0
    btw = 0

    for product in producten:
        productnaam = product.get('productnaam', 'Onbekend product')
        aantal = product.get('aantal', 0)
        prijs_per_stuk = product.get('prijs_per_stuk_excl_btw', 0)
        btw_percentage = product.get('btw_percentage', 0)

        # Prijs exclusief btw
        prijs_excl_btw = prijs_per_stuk * aantal
        totaal_prijs_excl_btw += prijs_excl_btw

        # Prijs inclusief btw
        prijs_incl_btw = prijs_excl_btw * (1 + (btw_percentage / 100))
        totaal_prijs_incl_btw += prijs_incl_btw

        # Bereken de BTW
        btw += prijs_incl_btw - prijs_excl_btw

        # Productinformatie op de PDF
        c.drawString(30, y_cordinaat, f"Product naam - {productnaam}")
        c.drawString(280, y_cordinaat, str(aantal))
        c.drawString(345, y_cordinaat, str(prijs_per_stuk))
        c.drawString(430, y_cordinaat, str(f"{btw_percentage}%"))
        y_cordinaat -= 20  # Verlaag de Y-coördinaat voor elk product

    # Klantgegevens
    c.drawString(100, 340, naam_klant)
    c.drawString(70, 320, aderes_klant)
    c.drawString(90, 300, postcode_klant)
    c.drawString(60, 280, stad_klant)
    c.drawString(120, 260, ordernummer)

    # Totaalprijzen
    c.drawString(279.5, 340, f"Totaal exclusief btw € {totaal_prijs_excl_btw:.2f}")
    c.drawString(279.5, 320, "Btw €")
    c.drawString(310, 320, f"{btw:.2f}")

    # Inclusief btw
    c.drawString(430, 230, "€")
    c.drawString(430, 230, f"€ {totaal_prijs_incl_btw:.2f}")

    # Dikgedrukte tekst
    c.setFont("Helvetica-Bold", 18)
    c.drawString(30, 620, "Factuur")

    # Categorieën van de factuur
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, 600, "Factuur nummer")
    c.drawString(145, 600, "Factuur datum")
    c.drawString(250, 600, "Betaaltermijn")
    c.drawString(30, 560, "KVK nummer")
    c.drawString(145, 560, "BTW nummer")
    c.drawString(250, 560, "Bank nummer")

    # Producten tabelkop
    c.drawString(30, 510, "Omschrijving")
    c.drawString(270, 510, "Aantal")
    c.drawString(335, 510, "Bedrag")
    c.drawString(420, 510, "Btw")

    # Klantgegevens kop
    c.drawString(30, 340, "Klant naam:")
    c.drawString(30, 320, "Adres:")
    c.drawString(30, 300, "Postcode:")
    c.drawString(30, 280, "Stad:")
    c.drawString(30, 260, "Order nummer:")

    # Totaal inclusief btw kop
    c.drawString(279.5, 230, f"Totaal inclusief btw")

    # Toon canvas
    c.showPage()

    # Sla canvas op
    c.save()
    
    # Oorspronkelijke locatie en doelmap
    pdf_path = os.path.join(os.path.dirname(__file__), file_name)  # Oorspronkelijke locatie
    new_pdf_path = os.path.join(output_folder, file_name)  # Doelmap

    # Controleer of het bestand al bestaat in de doelmap en verwijder het
    if os.path.exists(new_pdf_path):
        os.remove(new_pdf_path)  # Verwijder het bestaande bestand als het er al is

    # Verplaats de nieuwe PDF naar de doelmap
    os.rename(pdf_path, new_pdf_path)

    print(f"PDF {getal} is opgeslagen in {new_pdf_path}")
    getal += 1
