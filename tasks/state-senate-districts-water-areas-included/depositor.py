import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/7equ-j2vi?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/state-senate-districts-water-areas-included/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/state-senate-districts-water-areas-included/data.geojson"]
