import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/pp5b-95kq?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2013-2014-school-zones/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2013-2014-school-zones/data.geojson"]
