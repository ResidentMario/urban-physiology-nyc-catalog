import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/uyj8-7rv5?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/sandy-inundation-zone/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/sandy-inundation-zone/data.geojson"]
