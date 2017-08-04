import requests
r = requests.get("https://data.cityofnewyork.us/api/views/vc9y-jf25/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccr-annual-report/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccr-annual-report/data.csv"]
