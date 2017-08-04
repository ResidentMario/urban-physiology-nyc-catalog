import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/2mhq-um7h?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/city-owned-and-leased-property-colp-2/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/city-owned-and-leased-property-colp-2/data.geojson"]
