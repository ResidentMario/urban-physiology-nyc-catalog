import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/a9we-mtpn?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-wi-fi-hotspot-locations-2/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-wi-fi-hotspot-locations-2/data.geojson"]
