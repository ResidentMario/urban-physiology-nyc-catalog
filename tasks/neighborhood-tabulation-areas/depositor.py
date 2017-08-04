import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/cpf4-rkhq?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/neighborhood-tabulation-areas/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/neighborhood-tabulation-areas/data.geojson"]
