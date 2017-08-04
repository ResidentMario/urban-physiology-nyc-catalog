import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/g84h-jbjm?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/open-space-parks/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/open-space-parks/data.geojson"]
