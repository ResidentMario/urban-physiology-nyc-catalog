import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/j7ww-5ipv?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/swimming-pools/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/swimming-pools/data.geojson"]
