import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/6cne-um3h?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2000-census-blocks-water-areas-included/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2000-census-blocks-water-areas-included/data.geojson"]
