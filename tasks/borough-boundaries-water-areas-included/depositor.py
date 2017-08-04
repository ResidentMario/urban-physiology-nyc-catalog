import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/tv64-9x69?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/borough-boundaries-water-areas-included/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/borough-boundaries-water-areas-included/data.geojson"]
