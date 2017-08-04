import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/x9uq-u3qs?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/pavement-edge/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/pavement-edge/data.geojson"]
