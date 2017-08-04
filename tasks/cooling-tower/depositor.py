import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/miz8-534t?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/cooling-tower/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/cooling-tower/data.geojson"]
