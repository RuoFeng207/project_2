import os
import json
from termcolor import colored

# Bepaal de locatie van de scriptmap en JSON-map
file_path = os.path.dirname(__file__)  
json_location = os.path.join(file_path, "JSON_ORDER")  

print(f"Zoeken naar JSON-bestanden in: {json_location}")

# Controleer of de map bestaat
if os.path.exists(json_location) and os.path.isdir(json_location):
    # Lijst alle bestanden in de map
    json_bestanden = [bestandsnaam for bestandsnaam in os.listdir(json_location) if bestandsnaam.endswith(".json")]
    
    if json_bestanden:  # Controleer of er JSON-bestanden zijn
        for bestandsnaam in json_bestanden:  # Loop door alle JSON-bestanden
            bestandspad = os.path.join(json_location, bestandsnaam)

            with open(bestandspad, "r", encoding="utf-8") as file:
                data = json.load(file)  # Laad JSON in een dictionary

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

            # print(f"\nOrdernummer: {ordernummer}")
            # print(f"Orderdatum: {orderdatum}")
            # print(f"Betaaltermijn: {betaaltermijn}")
            # print(f"Klantnaam: {naam_klant}")
            # print(f"Klantadres: {aderes_klant}")
            # print(f"Klantpostcode: {postcode_klant}")
            # print(f"Klantstad: {stad_klant}")
            # print(f"KVK-nummer: {kvk_nummer}")

            producten = order.get("producten", [])
            totaal_prijs_incl_btw = 0

            for product in producten:
                productnaam = product.get("productnaam")
                aantal = product.get("aantal", 0)
                prijs_per_stuk = product.get("prijs_per_stuk_excl_btw", 0)
                btw_percentage = product.get("btw_percentage", 0)

                # Bereken de prijs exclusief BTW
                prijs_excl_btw = prijs_per_stuk * aantal

                # Bereken de prijs inclusief BTW
                prijs_incl_btw = prijs_excl_btw * (1 + (btw_percentage / 100))

                # Totaalprijs inclusief BTW bijhouden
                totaal_prijs_incl_btw += prijs_incl_btw

                # Bereken de BTW voor het huidige product
                btw = prijs_incl_btw - prijs_excl_btw

       

                # print(f"Productnaam: {productnaam}")
                # print(f"Aantal: {aantal}")
                # print(f"Prijs per stuk (excl. BTW): {prijs_per_stuk}")
                # print(f"BTW percentage: {btw_percentage}")
                # print(f"prijs exlusief btw{prijs_excl_btw}")
                # print(f"Prijs inclusief btw: {prijs_incl_btw:.2f}")
                # print("")
                # print(btw)
            # print(f"Totaal prijs inc btw: {totaal_prijs_incl_btw:.2f}")

    else:
        print(f"Er zijn {colored('geen', 'red', attrs=['bold'])} JSON-bestanden in de map.")
else:
    print(f"De map JSON_ORDER bestaat {colored('niet', 'red', attrs=['bold'])}.")