import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/hrii-hezj?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/botanical-gardens/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/botanical-gardens/data.geojson"]
