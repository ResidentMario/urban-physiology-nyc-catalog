import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/pckb-8r2z?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/open-space-other/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/open-space-other/data.geojson"]
