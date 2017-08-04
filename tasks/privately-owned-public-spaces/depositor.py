import requests
r = requests.get("https://data.cityofnewyork.us/download/fum3-ejky/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/privately-owned-public-spaces/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/privately-owned-public-spaces/data.zip"]
