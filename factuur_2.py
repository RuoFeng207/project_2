import os
import json
from termcolor import colored, cprint, COLORS

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
                print(f"{colored(" Gelezen","green",attrs=["bold"])}: {bestandsnaam}")
                print(data)  # Print de inhoud van het JSON-bestand

            order = data.get("order",{})
            ordernummer = order.get("ordernummer")
            orderdatum = order.get("orderdatum")
            betaaltermijn = order.get("betaaltermijn")
            klant = order.get("klant",{})
            naam_klant = klant.get("naam")
            aderes_klant = klant.get("adres")
            postcode_klant = klant.get("postcode")
            stad_klant = klant.get("stad")
            kvk_nummer = klant.get("KVK-nummer")
            print("")
            print("")
            print(f"Ordernummer: {ordernummer}")
            print(f"Orderdatum: {orderdatum}")
            print(f"Betaaltermijn: {betaaltermijn}")
            print(f"Klantnaam: {naam_klant}")
            print(f"Klantadres: {aderes_klant}")
            print(f"Klantpostcode: {postcode_klant}")
            print(f"Klantstad: {stad_klant}")
            print(f"KVK-nummer: {kvk_nummer}")
            print("")

            producten = order.get("producten", [])
            for product in producten:
                productnaam = product.get("productnaam")
                aantal = product.get("aantal")
                prijs_per_stuk = product.get("prijs_per_stuk_excl_btw")
                btw_percentage = product.get("btw_percentage")
                
                print(f"Productnaam: {productnaam}")
                print(f"Aantal: {aantal}")
                print(f"Prijs per stuk (excl. BTW): {prijs_per_stuk}")
                print(f"BTW percentage: {btw_percentage}")
                
    
                
                
    else:
        print(f"Er zijn {colored("geen","red",attrs=["bold"])} JSON-bestanden in de map.")
else:
    print(f"De map JSON_ORDER bestaat {colored("niet","red",attrs=["bold"])}.")