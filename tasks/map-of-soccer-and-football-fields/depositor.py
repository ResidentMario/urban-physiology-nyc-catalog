import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/qqsi-vm9f?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/map-of-soccer-and-football-fields/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/map-of-soccer-and-football-fields/data.geojson"]
