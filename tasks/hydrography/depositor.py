import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/drh3-e2fd?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hydrography/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hydrography/data.geojson"]
