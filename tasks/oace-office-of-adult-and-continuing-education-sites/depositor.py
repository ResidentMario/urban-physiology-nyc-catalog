import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/4u36-44pe?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/oace-office-of-adult-and-continuing-education-sites/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/oace-office-of-adult-and-continuing-education-sites/data.geojson"]
