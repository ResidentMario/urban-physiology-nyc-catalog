import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/3vjv-6tf5?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/pools/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/pools/data.geojson"]
