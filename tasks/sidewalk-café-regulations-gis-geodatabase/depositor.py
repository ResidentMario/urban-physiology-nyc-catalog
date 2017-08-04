import requests
r = requests.get("https://data.cityofnewyork.us/download/mran-v46w/application%2Fzip")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/sidewalk-café-regulations-gis-geodatabase/data.zip", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/sidewalk-café-regulations-gis-geodatabase/data.zip"]
