import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/ikvd-dex8?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/curbs/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/curbs/data.geojson"]
