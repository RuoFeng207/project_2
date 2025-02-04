import json
import os 

pad = os.path.abspath(".")   # 
json_pad = os.path.join(pad, "JSON_ORDER") # map aanroepen
print(json_pad)
print(pad)
 
def pdf(bestand):        # funtctie maken 
    with open(bestand)as f:
        gegeven= json.load(f)
        print(gegeven)     # json key bijvoegen


for bestand in os.listdir(json_pad): # loop de functie pdf
    pdf(os.path.join(json_pad,bestand))
    