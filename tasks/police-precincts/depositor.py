import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/78dh-3ptz?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/police-precincts/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/police-precincts/data.geojson"]
