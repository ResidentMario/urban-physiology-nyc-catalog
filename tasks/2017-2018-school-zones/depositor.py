import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/ghq4-ydq4?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2017-2018-school-zones/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2017-2018-school-zones/data.geojson"]
