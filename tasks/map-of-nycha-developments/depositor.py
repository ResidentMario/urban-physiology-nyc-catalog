import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/i9rv-hdr5?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/map-of-nycha-developments/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/map-of-nycha-developments/data.geojson"]
