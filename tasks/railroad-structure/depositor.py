import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/5dic-xnxs?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/railroad-structure/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/railroad-structure/data.geojson"]
