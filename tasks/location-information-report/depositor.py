import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ig6g-qauv/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/location-information-report/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/location-information-report/data.csv"]
