import requests
r = requests.get("https://data.cityofnewyork.us/download/mm69-vrje/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/zoning-gis-data-geodatabase/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/zoning-gis-data-geodatabase/data.zip"]
