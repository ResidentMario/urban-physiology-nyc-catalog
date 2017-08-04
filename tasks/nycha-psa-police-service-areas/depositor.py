import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/72wx-vdjr?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycha-psa-police-service-areas/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycha-psa-police-service-areas/data.geojson"]
