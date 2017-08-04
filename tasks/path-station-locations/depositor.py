import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/acxp-7ep7?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/path-station-locations/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/path-station-locations/data.geojson"]
