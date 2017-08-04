import requests
r = requests.get("https://data.cityofnewyork.us/api/views/a9md-ynri/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/civil-service-list-certification/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/civil-service-list-certification/data.csv"]
