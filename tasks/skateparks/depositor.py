import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/kjtf-e6kp?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/skateparks/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/skateparks/data.geojson"]
