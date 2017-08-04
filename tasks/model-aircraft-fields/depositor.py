import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/asbw-cwm7?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/model-aircraft-fields/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/model-aircraft-fields/data.geojson"]
