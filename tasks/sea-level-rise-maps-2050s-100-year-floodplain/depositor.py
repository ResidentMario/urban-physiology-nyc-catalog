import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/hbw8-2bah?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/sea-level-rise-maps-2050s-100-year-floodplain/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/sea-level-rise-maps-2050s-100-year-floodplain/data.geojson"]
