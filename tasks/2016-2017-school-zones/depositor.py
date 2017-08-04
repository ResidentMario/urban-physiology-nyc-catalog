import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/ux7j-iww6?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2016-2017-school-zones/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2016-2017-school-zones/data.geojson"]
