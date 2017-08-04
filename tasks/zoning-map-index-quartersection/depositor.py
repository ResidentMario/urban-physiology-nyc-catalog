import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/58k2-kgtb?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/zoning-map-index-quartersection/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/zoning-map-index-quartersection/data.geojson"]
