import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/pv8j-5ywy?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/map-of-nycha-community-facilities/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/map-of-nycha-community-facilities/data.geojson"]
