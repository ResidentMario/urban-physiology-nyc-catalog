import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/r8nu-ymqj?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-districts/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-districts/data.geojson"]
