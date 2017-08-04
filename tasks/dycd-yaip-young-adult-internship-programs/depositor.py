import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/s2d8-h5fg?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-yaip-young-adult-internship-programs/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-yaip-young-adult-internship-programs/data.geojson"]
