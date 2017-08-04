import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/7vpq-4bh4?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/municipal-court-districts/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/municipal-court-districts/data.geojson"]
