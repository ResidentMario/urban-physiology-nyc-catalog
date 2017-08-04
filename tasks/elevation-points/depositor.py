import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/szwg-xci6?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/elevation-points/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/elevation-points/data.geojson"]
