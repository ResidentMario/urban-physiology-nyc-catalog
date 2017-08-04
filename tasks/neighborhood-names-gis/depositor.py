import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/99bc-9p23?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/neighborhood-names-gis/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/neighborhood-names-gis/data.geojson"]
