import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/2n64-63dq?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-osy-out-of-school-youth/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-osy-out-of-school-youth/data.geojson"]
