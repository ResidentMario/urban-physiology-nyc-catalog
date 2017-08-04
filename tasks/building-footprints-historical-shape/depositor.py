import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/s5zg-yzea?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/building-footprints-historical-shape/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/building-footprints-historical-shape/data.geojson"]
