import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/27b5-th78?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/median/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/median/data.geojson"]
