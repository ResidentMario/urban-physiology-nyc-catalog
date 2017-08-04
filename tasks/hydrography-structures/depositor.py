import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/53au-zf7x?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hydrography-structures/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hydrography-structures/data.geojson"]
