import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/vfx9-tbb6?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/sidewalk/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/sidewalk/data.geojson"]
