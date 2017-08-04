import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/gx7x-82rk?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2010-census-tracts-water-areas-included/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2010-census-tracts-water-areas-included/data.geojson"]
