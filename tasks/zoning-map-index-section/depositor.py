import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/bpt7-i8t8?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/zoning-map-index-section/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/zoning-map-index-section/data.geojson"]
