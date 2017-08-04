import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/xiyt-f6tz?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycdcp-manhattan-bike-count-locations/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nycdcp-manhattan-bike-count-locations/data.geojson"]
