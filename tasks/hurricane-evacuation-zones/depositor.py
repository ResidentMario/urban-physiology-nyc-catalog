import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/uihr-hn7s?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hurricane-evacuation-zones/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hurricane-evacuation-zones/data.geojson"]
