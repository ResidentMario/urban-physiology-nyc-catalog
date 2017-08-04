import requests
r = requests.get("https://data.cityofnewyork.us/api/views/g7ir-4pf8/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/law-speeches/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/law-speeches/data.csv"]
