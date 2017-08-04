import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/mzpm-a6vd?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/community-districts-water-areas-included/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/community-districts-water-areas-included/data.geojson"]
