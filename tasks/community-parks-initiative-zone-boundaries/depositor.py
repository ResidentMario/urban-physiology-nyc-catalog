import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/vvdx-b56i?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/community-parks-initiative-zone-boundaries/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/community-parks-initiative-zone-boundaries/data.geojson"]
