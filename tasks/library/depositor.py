import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/p4pf-fyc4?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/library/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/library/data.geojson"]
