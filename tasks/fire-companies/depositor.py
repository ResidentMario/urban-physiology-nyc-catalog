import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/iiv7-jaj9?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fire-companies/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fire-companies/data.geojson"]
