import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/gpxw-bq7a?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/post-office/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/post-office/data.geojson"]
