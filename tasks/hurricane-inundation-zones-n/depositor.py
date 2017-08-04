import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/pask-bcmz?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hurricane-inundation-zones-n/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hurricane-inundation-zones-n/data.geojson"]
