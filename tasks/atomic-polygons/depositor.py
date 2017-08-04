import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/djze-f4qi?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/atomic-polygons/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/atomic-polygons/data.geojson"]
