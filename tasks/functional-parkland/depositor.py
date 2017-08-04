import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/e3uq-vht9?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/functional-parkland/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/functional-parkland/data.geojson"]
