import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/a9xv-vek9?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/sidewalk-centerline/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/sidewalk-centerline/data.geojson"]
