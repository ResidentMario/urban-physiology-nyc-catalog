import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/yqz9-aduk?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-syep-summer-youth-employment/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-syep-summer-youth-employment/data.geojson"]
