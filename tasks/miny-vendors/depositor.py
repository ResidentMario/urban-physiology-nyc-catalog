import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/79z8-9mcf?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/miny-vendors/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/miny-vendors/data.geojson"]
