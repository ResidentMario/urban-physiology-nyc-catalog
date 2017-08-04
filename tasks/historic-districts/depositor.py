import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/xbvj-gfnw?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/historic-districts/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/historic-districts/data.geojson"]
