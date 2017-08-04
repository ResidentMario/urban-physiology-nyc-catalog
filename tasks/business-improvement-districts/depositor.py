import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/ejxk-d93y?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/business-improvement-districts/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/business-improvement-districts/data.geojson"]
