import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/2cav-chmn?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/street-pavement-rating/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/street-pavement-rating/data.geojson"]
