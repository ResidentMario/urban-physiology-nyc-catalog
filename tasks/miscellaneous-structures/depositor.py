import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/7acq-q3tq?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/miscellaneous-structures/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/miscellaneous-structures/data.geojson"]
