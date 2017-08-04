import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/exjm-f27b?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-street-centerline-cscl/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-street-centerline-cscl/data.geojson"]
