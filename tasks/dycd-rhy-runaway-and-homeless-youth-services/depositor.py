import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/h682-ywyg?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-rhy-runaway-and-homeless-youth-services/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-rhy-runaway-and-homeless-youth-services/data.geojson"]
