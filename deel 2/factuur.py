import json

with open("C:/School/Software Development/Projecten/project_2/deel 2/test_set_softwareleverancier/2000-018.json", "r") as f:
    data = json.load(f)

print(data)
orderdatum = data["order"]["orderdatum"]
