import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/rjaj-zgq7?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/parks-properties/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/parks-properties/data.geojson"]
