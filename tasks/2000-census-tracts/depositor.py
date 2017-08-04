import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/ysjj-vb9j?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2000-census-tracts/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2000-census-tracts/data.geojson"]
