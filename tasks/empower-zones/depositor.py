import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/khkb-h6hx?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/empower-zones/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/empower-zones/data.geojson"]
