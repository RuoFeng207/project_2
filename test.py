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
                print(f"✅ Gelezen: {bestandsnaam}")
                print(data)  # Print de inhoud van het JSON-bestand

                order = data.get("order",{})
                
                producten = order.get("producten", [])
                for product in producten:
                    productnaam = product.get("productnaam")
                    aantal = product.get("aantal")
                    prijs_per_stuk = product.get("prijs_per_stuk_excl_btw")
                    btw_percentage = product.get("btw_percentage")
                    
                
    else:
        print("❌ Er zijn geen JSON-bestanden in de map.")
else:
    print("❌ De map JSON_ORDER bestaat niet of is geen directory.")