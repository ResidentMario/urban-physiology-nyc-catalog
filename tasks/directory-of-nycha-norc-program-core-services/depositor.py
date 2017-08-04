import requests
r = requests.get("https://data.cityofnewyork.us/api/views/39pe-uzy3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-nycha-norc-program-core-services/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-nycha-norc-program-core-services/data.csv"]
