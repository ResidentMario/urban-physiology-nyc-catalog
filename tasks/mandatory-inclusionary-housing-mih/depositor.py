import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/bw8v-wzdr?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/mandatory-inclusionary-housing-mih/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/mandatory-inclusionary-housing-mih/data.geojson"]
