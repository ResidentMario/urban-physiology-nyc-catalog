import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/vr8g-vfny?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/milliontreesnyc-block-planting-locations/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/milliontreesnyc-block-planting-locations/data.geojson"]
