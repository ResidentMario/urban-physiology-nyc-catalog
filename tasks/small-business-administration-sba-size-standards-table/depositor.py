import requests
r = requests.get("https://data.cityofnewyork.us/api/views/y52e-hp89/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/small-business-administration-sba-size-standards-table/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/small-business-administration-sba-size-standards-table/data.csv"]
