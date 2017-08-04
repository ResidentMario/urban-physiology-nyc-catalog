import requests
r = requests.get("https://data.cityofnewyork.us/download/sg2s-hjt6/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/adopt-a-tree-inventory/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/adopt-a-tree-inventory/data.zip"]
