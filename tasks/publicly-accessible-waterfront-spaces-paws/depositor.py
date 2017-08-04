import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/388s-pnvc?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/publicly-accessible-waterfront-spaces-paws/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/publicly-accessible-waterfront-spaces-paws/data.geojson"]
