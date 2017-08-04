import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ye3c-m4ga/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/civil-list/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/civil-list/data.csv"]
