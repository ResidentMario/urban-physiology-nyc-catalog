import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/n3et-mfjw?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-beacon/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-beacon/data.geojson"]
