import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/d7n3-sf2d?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/path-line/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/path-line/data.geojson"]
