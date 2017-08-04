import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/q6ei-tvmg?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dsny-special-waste/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dsny-special-waste/data.geojson"]
