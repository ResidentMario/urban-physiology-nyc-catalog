import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/w83z-2kf9?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inclusionary-housing-designated-areas/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inclusionary-housing-designated-areas/data.geojson"]
