import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/3aim-ipk8?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/empire-zones/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/empire-zones/data.geojson"]
