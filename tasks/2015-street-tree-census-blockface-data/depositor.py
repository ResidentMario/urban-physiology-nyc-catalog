import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/2cd9-59fr?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2015-street-tree-census-blockface-data/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2015-street-tree-census-blockface-data/data.geojson"]
