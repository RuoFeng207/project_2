import os
import json

# Bepaal de locatie van de huidige scriptmap
file_path = os.path.dirname(__file__)  
json_location = os.path.join(file_path, "JSON_ORDER")  # Map met JSON-bestanden

print(f"Zoeken naar JSON-bestanden in: {json_location}")

# Controleer of de map bestaat
if os.path.exists(json_location) and os.path.isdir(json_location):
    json_data = {}  # Dictionary om alle JSON-bestanden op te slaan

    # Loop door alle bestanden in de map
    for bestandsnaam in os.listdir(json_location):
        if bestandsnaam.endswith(".json"):  # Alleen JSON-bestanden openen
            bestandspad = os.path.join(json_location, bestandsnaam)
            
            with open(bestandspad, "r", encoding="utf-8") as file:
                data = json.load(file)  # Laad JSON in een dictionary
                json_data[bestandsnaam] = data  # Opslaan in een dictionary met de bestandsnaam als sleutel
            
            print(f"✅ Gelezen: {bestandsnaam}")

    # Print alle ingelezen JSON-bestanden
    print("\nAlle JSON-data:")
    print(json_data)
else:
    print("❌ De map JSON_ORDER bestaat niet of is geen directory.")