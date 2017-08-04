import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/uvgd-xsc8?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/retaining-wall/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/retaining-wall/data.geojson"]
