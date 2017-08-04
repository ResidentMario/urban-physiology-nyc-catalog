import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/6ej9-7qyi?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/after-school-programs/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/after-school-programs/data.geojson"]
