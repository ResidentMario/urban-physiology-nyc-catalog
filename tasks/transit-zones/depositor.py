import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/cpcf-tcxs?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/transit-zones/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/transit-zones/data.geojson"]
