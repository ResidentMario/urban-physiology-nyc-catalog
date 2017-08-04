import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/4p5v-sqmv?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/map-of-nycha-community-engagement-partnership-zones/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/map-of-nycha-community-engagement-partnership-zones/data.geojson"]
