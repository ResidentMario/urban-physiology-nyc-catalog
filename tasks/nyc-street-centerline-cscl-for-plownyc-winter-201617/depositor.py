import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/uxpt-rzip?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-street-centerline-cscl-for-plownyc-winter-201617/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-street-centerline-cscl-for-plownyc-winter-201617/data.geojson"]
