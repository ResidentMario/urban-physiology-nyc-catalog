import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/arq3-7z49?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/subway-stations/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/subway-stations/data.geojson"]
