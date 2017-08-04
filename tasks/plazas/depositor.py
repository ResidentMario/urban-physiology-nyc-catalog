import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/m4mp-ji5y?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/plazas/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/plazas/data.geojson"]
