import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/gi7d-8gt5?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/scenic-landmarks/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/scenic-landmarks/data.geojson"]
