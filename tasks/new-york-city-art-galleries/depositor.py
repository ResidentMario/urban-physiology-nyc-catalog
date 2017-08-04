import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/tgyc-r5jh?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-art-galleries/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-art-galleries/data.geojson"]
