import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/rxuy-2muj?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/points-of-interest/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/points-of-interest/data.geojson"]
