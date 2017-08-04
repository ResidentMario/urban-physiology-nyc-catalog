import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/yann-8etk?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/athletic-facilities/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/athletic-facilities/data.geojson"]
