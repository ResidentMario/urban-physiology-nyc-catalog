import requests
r = requests.get("https://data.cityofnewyork.us/api/views/yk6f-pa7p/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/law-public-service-program/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/law-public-service-program/data.csv"]
