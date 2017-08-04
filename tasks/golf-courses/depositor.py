import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/rjqi-t95z?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/golf-courses/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/golf-courses/data.geojson"]
