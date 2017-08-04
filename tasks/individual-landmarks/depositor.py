import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/ch5p-r223?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/individual-landmarks/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/individual-landmarks/data.geojson"]
