import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/ye4j-rp7z?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2005-street-tree-census/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2005-street-tree-census/data.geojson"]
