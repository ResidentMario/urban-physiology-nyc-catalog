import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ci93-uc8s/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/mwbe-lbe-and-ebe-certified-business-list/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/mwbe-lbe-and-ebe-certified-business-list/data.csv"]
