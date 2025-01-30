import json

with open("C:/School/Software Development/Projecten/project_2/deel 2/test_set_softwareleverancier/2022-853.json", "r") as f:
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
producten = producten.pop(0)
product_naam = producten["productnaam"]
product_aantal = producten["aantal"]
product_prijs = producten["prijs_per_stuk_excl_btw"]
product_btw_procent = producten["btw_percentage"]
product_totprijs = product_aantal * product_prijs
if product_btw_procent == 6:
    product_btwprijs = ((product_totprijs / 100) * 106) - product_totprijs
elif product_btw_procent == 9:
    product_btwprijs = ((product_totprijs / 100) * 109) - product_totprijs
elif product_btw_procent == 21:
    product_btwprijs = ((product_totprijs / 100) * 121) - product_totprijs
print(product_btwprijs)