import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/im58-6hb9?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/spray-showers/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/spray-showers/data.geojson"]
