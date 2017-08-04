import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/2qj2-cctx?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/shoreline/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/shoreline/data.geojson"]
