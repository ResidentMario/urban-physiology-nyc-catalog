import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/b55q-34ps?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/health-center-districts/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/health-center-districts/data.geojson"]
