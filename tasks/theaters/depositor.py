import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/kdu2-865w?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/theaters/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/theaters/data.geojson"]
