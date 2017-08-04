import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/qvtg-k2hn?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/beaches/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/beaches/data.geojson"]
