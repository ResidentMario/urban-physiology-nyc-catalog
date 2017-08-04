import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/g6pj-hd8k?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-address-points/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-address-points/data.geojson"]
