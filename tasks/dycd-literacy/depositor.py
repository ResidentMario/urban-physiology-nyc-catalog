import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/ty8z-v9d2?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-literacy/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-literacy/data.geojson"]
