import json
import os
file_path = os.path.dirname(__file__)
json_location = os.path.join(file_path, "2000-096.json")
with open(json_location, "r") as f:
    data = json.load(f)
    
order = data["order"]
ordernummer = order["ordernummer"]
orderdatum = order["orderdatum"]
klant = order["klant"]
klant_naam = klant["naam"]
klant_adres = klant["adres"]
klant_postcode = klant["postcode"]
klant_stad = klant["stad"]
klant_KVK = klant["KVK-nummer"]
producten = order["producten"]
productnamen = []
aantallen = []
prijzen_excl_btw = []
btw_percentages = []
totale_prijzen_incl_btw = []

for product in producten:
    productnaam = product["productnaam"]
    aantal = product["aantal"]
    prijs_per_stuk = product["prijs_per_stuk_excl_btw"]
    btw_percentage = product["btw_percentage"]
    totale_prijs_excl_btw = aantal * prijs_per_stuk
    totale_prijs_incl_btw = totale_prijs_excl_btw * (1 + (btw_percentage / 100))
    
    productnamen.append(productnaam)
    aantallen.append(aantal)
    prijzen_excl_btw.append(prijs_per_stuk)
    btw_percentages.append(btw_percentage)
    totale_prijzen_incl_btw.append(totale_prijs_incl_btw)