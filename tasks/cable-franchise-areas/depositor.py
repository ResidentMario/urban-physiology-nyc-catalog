import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/fw3w-apxs?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/cable-franchise-areas/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/cable-franchise-areas/data.geojson"]
