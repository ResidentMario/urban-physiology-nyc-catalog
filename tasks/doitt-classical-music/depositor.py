import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/txxa-5nhg?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doitt-classical-music/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doitt-classical-music/data.geojson"]
