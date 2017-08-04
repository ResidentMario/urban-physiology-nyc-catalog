import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/i7a5-bsik?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/railroad-line/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/railroad-line/data.geojson"]
