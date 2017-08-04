import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/4kym-4xw5?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/colleges-and-universities/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/colleges-and-universities/data.geojson"]
