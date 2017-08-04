import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/xgwd-7vhd?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/roadbed/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/roadbed/data.geojson"]
