import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/t7sx-id53?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/public-pay-telephone-locations/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/public-pay-telephone-locations/data.geojson"]
