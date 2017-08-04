import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/rm4p-5usz?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/universal-pre-k/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/universal-pre-k/data.geojson"]
