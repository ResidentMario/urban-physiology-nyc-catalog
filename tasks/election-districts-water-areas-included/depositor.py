import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/wue3-68ab?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/election-districts-water-areas-included/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/election-districts-water-areas-included/data.geojson"]
