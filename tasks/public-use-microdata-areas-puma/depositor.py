import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/cwiz-gcty?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/public-use-microdata-areas-puma/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/public-use-microdata-areas-puma/data.geojson"]
