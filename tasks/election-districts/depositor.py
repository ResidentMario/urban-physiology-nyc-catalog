import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/h2n3-98hq?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/election-districts/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/election-districts/data.geojson"]
