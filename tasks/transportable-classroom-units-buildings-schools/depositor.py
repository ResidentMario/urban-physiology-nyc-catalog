import requests
r = requests.get("https://data.cityofnewyork.us/api/views/gshi-yqza/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/transportable-classroom-units-buildings-schools/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/transportable-classroom-units-buildings-schools/data.csv"]
