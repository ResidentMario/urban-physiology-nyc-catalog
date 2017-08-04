import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/qd3c-zuu7?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/congressional-districts/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/congressional-districts/data.geojson"]
