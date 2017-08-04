import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/u6su-4fpt?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/stealth-fiber-map/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/stealth-fiber-map/data.geojson"]
