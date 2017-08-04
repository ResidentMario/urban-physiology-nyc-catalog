import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/e2f7-cs7i?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/parking-lots/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/parking-lots/data.geojson"]
