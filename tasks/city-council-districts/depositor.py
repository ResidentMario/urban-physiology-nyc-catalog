import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/yusd-j4xi?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/city-council-districts/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/city-council-districts/data.geojson"]
