import requests
r = requests.get("https://data.cityofnewyork.us/download/c2g8-ercv/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/city-owned-and-leased-property-colp/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/city-owned-and-leased-property-colp/data.zip"]
