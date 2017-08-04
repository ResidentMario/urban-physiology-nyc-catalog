import requests
r = requests.get("https://data.cityofnewyork.us/api/views/a9f5-j694/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/aging-services/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/aging-services/data.csv"]
