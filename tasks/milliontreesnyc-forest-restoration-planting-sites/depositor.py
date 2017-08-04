import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/pn7c-bqri?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/milliontreesnyc-forest-restoration-planting-sites/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/milliontreesnyc-forest-restoration-planting-sites/data.geojson"]
