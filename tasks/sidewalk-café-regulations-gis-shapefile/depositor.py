import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/qsuf-mgjh?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/sidewalk-café-regulations-gis-shapefile/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/sidewalk-café-regulations-gis-shapefile/data.geojson"]
