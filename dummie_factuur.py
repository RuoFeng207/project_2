import json
import os

file_path = os.path.dirname(__file__)
json_location = os.path.join(file_path, "2000-096.json")

with open(json_location, "r") as f:
    data = json.load(f)

order = data["order"]
ordernummer = order["ordernummer"]
orderdatum = order["orderdatum"]
betaaltermijn = order["betaaltermijn"]
klant = order["klant"]
klant_naam = klant["naam"]
klant_adres = klant["adres"]
klant_postcode = klant["postcode"]
klant_stad = klant["stad"]
klant_KVK = klant["KVK-nummer"]
producten = order["producten"]

# Lists to store data
productnamen = []
aantallen = []
prijzen_excl_btw = []
btw_percentages = []
totale_prijzen_incl_btw1 = []
totale_prijzen_excl_btw1 = []
prijzen = []
hoeveel = []

for product in producten:
    # Process multiple products
    productnaam = product["productnaam"]
    aantal = product["aantal"]
    prijs_per_stuk = product["prijs_per_stuk_excl_btw"]
    btw_percentage = product["btw_percentage"]
    totale_prijs_excl_btw = aantal * prijs_per_stuk
    totale_prijs_incl_btw = totale_prijs_excl_btw * (1 + (btw_percentage / 100))
    
    # Append values to the lists
    totale_prijzen_incl_btw1.append(totale_prijs_incl_btw)
    productnamen.append(productnaam)
    aantallen.append(aantal)
    prijzen_excl_btw.append(prijs_per_stuk)
    btw_percentages.append(btw_percentage)
    totale_prijzen_excl_btw1.append(totale_prijs_excl_btw)
    
    # Placeholder for counting
    hoeveel.append("ha")

# Create copies for calculation
totale_prijzen_excl_btw2 = totale_prijzen_excl_btw1.copy()
totale_prijzen_incl_btw2 = totale_prijzen_incl_btw1.copy()

# Initialize totals
prijzenTot = 0
totale_prijs = 0

# Loop to calculate totals excluding VAT
while len(totale_prijzen_excl_btw2) > 0:
    prijs = totale_prijzen_excl_btw2.pop(0)
    prijzenTot += prijs  # Use += to accumulate the price

# Loop to calculate totals including VAT
while len(totale_prijzen_incl_btw2) > 0:
    prijs = totale_prijzen_incl_btw2.pop(0)
    totale_prijs += prijs  # Use += to accumulate the price

# If there are multiple products, process them accordingly
if len(hoeveel) == 1:
    product1 = productnamen.pop(0)
    aantal1 = str(aantallen.pop(0))
    prijszonder1 = str(prijzen_excl_btw.pop(0))
    btw1 = str(btw_percentages.pop(0))
    prijstotbtw1 = totale_prijzen_incl_btw1.pop(0)
    prijstot1 = totale_prijzen_excl_btw1.pop(0)
    prijsbtw = prijstotbtw1 - prijstot1
    print(f"Product: {product1}, Aantal: {aantal1}, Prijs excl BTW: {prijszonder1}, BTW: {btw1}, Totaal incl BTW: {prijstotbtw1}, Totaal excl BTW: {prijstot1}, BTW: {prijsbtw}")

    if len(hoeveel) == 2:
        product2 = productnamen.pop(0)
        aantal2 = str(aantallen.pop(0))
        prijszonder2 = str(prijzen_excl_btw.pop(0))
        btw2 = str(btw_percentages.pop(0))
        prijstotbtw2 = totale_prijzen_incl_btw1.pop(0)
        prijstot2 = totale_prijzen_excl_btw1.pop(0)
        prijsbtw = prijstotbtw2 - prijstot2
        print(f"Product: {product2}, Aantal: {aantal2}, Prijs excl BTW: {prijszonder2}, BTW: {btw2}, Totaal incl BTW: {prijstotbtw2}, Totaal excl BTW: {prijstot2}, BTW: {prijsbtw}")

        if len(hoeveel) == 3:
            product3 = productnamen.pop(0)
            aantal3 = str(aantallen.pop(0))
            prijszonder3 = str(prijzen_excl_btw.pop(0))
            btw3 = str(btw_percentages.pop(0))
            prijstotbtw3 = totale_prijzen_incl_btw1.pop(0)
            prijstot3 = totale_prijzen_excl_btw1.pop(0)
            prijsbtw = prijstotbtw3 - prijstot3
            print(f"Product: {product3}, Aantal: {aantal3}, Prijs excl BTW: {prijszonder3}, BTW: {btw3}, Totaal incl BTW: {prijstotbtw3}, Totaal excl BTW: {prijstot3}, BTW: {prijsbtw}")
