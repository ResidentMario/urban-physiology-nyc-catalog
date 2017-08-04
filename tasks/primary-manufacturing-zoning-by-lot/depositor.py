import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/kxg8-856s?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/primary-manufacturing-zoning-by-lot/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/primary-manufacturing-zoning-by-lot/data.geojson"]
