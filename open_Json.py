import json
import os 


pad = os.path.abspath(".")   # 
json_pad = os.path.join(pad, "JSON_ORDER") # map aanroepen
print(json_pad)
print(pad)
 
def pdf(bestand):        # funtctie maken 
    try:
        with open(bestand,encoding="utf-8")as f:
            gegeven= json.load(f)
            print(gegeven)     # json key bijvoegen
    except Exception as fout:
        print(f"Er zit een fout bij {fout}")
    


for bestand in os.listdir(json_pad): # loop de functie pdf
    pdf(os.path.join(json_pad,bestand))
