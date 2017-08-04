import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/8ztn-rmii?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2015-2016-school-zones/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2015-2016-school-zones/data.geojson"]
