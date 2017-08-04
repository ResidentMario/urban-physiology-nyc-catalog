import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/d9z4-v86m?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/waterfront-access-plans/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/waterfront-access-plans/data.geojson"]
