import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/tar7-vww3?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-jersey-transit-station/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-jersey-transit-station/data.geojson"]
