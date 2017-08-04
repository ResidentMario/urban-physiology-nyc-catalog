import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/ekax-ky3z?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-museums/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-museums/data.geojson"]
