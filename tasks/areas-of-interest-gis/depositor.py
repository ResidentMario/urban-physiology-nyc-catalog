import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/mzbd-kucq?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/areas-of-interest-gis/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/areas-of-interest-gis/data.geojson"]
