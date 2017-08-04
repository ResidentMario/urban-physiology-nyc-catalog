import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/eizi-ujye?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nypd-sectors/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nypd-sectors/data.geojson"]
