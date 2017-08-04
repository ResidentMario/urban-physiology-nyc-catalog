import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/3qz8-muuu?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/subway-lines/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/subway-lines/data.geojson"]
