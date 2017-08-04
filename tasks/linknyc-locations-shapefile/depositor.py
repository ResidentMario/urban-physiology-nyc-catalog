import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/7b32-6xny?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/linknyc-locations-shapefile/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/linknyc-locations-shapefile/data.geojson"]
