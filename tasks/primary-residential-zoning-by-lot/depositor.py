import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/ieyi-rqsn?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/primary-residential-zoning-by-lot/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/primary-residential-zoning-by-lot/data.geojson"]
