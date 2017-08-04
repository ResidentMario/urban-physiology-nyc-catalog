import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/5p78-k3zm?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/health-areas/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/health-areas/data.geojson"]
