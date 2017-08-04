import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/v9xd-tt3e?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2010-census-blocks-water-areas-included/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2010-census-blocks-water-areas-included/data.geojson"]
