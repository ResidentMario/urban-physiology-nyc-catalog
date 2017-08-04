import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/bmax-4kci?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2000-census-tracts-water-areas-included/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2000-census-tracts-water-areas-included/data.geojson"]
