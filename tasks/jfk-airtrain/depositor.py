import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/3w3r-v568?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/jfk-airtrain/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/jfk-airtrain/data.geojson"]
