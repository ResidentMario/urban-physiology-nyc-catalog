import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/7vu2-3skk?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hurricane-inundation-zones-wnw/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hurricane-inundation-zones-wnw/data.geojson"]
