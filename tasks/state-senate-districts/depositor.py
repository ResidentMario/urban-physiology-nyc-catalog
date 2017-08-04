import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/h4i2-acfi?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/state-senate-districts/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/state-senate-districts/data.geojson"]
