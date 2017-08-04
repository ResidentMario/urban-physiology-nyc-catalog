import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/pf5b-73bw?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/state-assembly-districts/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/state-assembly-districts/data.geojson"]
