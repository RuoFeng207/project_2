import os
import json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf(data, output_file):
    c = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4

    # Achtergrond
    image_path2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "project_2pdf.png")
    c.drawImage(image_path2, 0, 0, width, height)

    # Logo
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sskills.png")
    c.drawImage(image_path, 280, 600, 290, 110)

    # Lijnen
    c.line(0, 505, 595, 505)
    c.line(0, 361, 595, 361)
    c.line(279.5, 250, 595, 250)

    # Bedrijfsinformatie
    c.setFont("Helvetica", 11)
    c.drawString(30, 690, "Adres: Europasingel 102693 GW Wervershoof")
    c.drawString(30, 670, "Tel: 06-51944831")
    c.drawString(30, 650, "E mail: SSkills@info.com")

    # Factuurinformatie
    c.drawString(30, 580, data.get("ordernummer", ""))
    c.drawString(145, 580, "28 januari 2025")  # Factuurdatum kan dynamisch worden gemaakt
    c.drawString(250, 580, "1 juni 2025")  # Vervaldatum kan dynamisch worden gemaakt

    # Klantinformatie
    c.drawString(100, 340, data.get("klant_naam", ""))
    c.drawString(70, 320, data.get("klant_adres", ""))
    c.drawString(90, 300, data.get("klant_postcode", ""))
    c.drawString(60, 280, data.get("klant_stad", ""))

    # Productinformatie
    y_position = 490
    for i in range(1, 4):  # Voor maximaal 3 producten
        product_key = f"product{i}"
        aantal_key = f"aantal{i}"
        prijs_key = f"prijszonder{i}"
        btw_key = f"btw{i}"
        
        if data.get(product_key):
            c.drawString(30, y_position, f"Geleverd product - {data[product_key]}")
            c.drawString(270, y_position, data.get(aantal_key, ""))
            c.drawString(335, y_position, data.get(prijs_key, ""))
            c.drawString(420, y_position, data.get(btw_key, ""))
            y_position -= 20

    # Totaal
    c.drawString(279.5, 340, f"Totaal exclusief btw € {data.get('prijzenTot', '')}")
    c.drawString(310, 320, f"{data.get('prijsbtw', '')}")
    c.drawString(430, 230, f"€ {data.get('totale_prijs', '')}")

    # Opslaan
    c.showPage()
    c.save()
    print(f"Je PDF is opgeslagen in {output_file}")

def main():
    json_pad = os.path.join(os)