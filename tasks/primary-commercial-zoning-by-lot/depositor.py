import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/pwhj-ikym?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/primary-commercial-zoning-by-lot/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/primary-commercial-zoning-by-lot/data.geojson"]
