import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/uh7r-6nya?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fire-battalions/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fire-battalions/data.geojson"]
