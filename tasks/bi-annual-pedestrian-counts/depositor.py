import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/2de2-6x2h?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/bi-annual-pedestrian-counts/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/bi-annual-pedestrian-counts/data.geojson"]
