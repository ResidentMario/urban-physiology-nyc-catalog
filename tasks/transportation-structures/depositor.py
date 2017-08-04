import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/h9sf-7bej?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/transportation-structures/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/transportation-structures/data.geojson"]
