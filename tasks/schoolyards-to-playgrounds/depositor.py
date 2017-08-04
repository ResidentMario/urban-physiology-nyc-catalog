import requests
r = requests.get("https://data.cityofnewyork.us/api/geospatial/urxm-vzzk?method=export&format=GeoJSON")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/schoolyards-to-playgrounds/data.geojson", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/schoolyards-to-playgrounds/data.geojson"]
