import requests
r = requests.get("https://data.cityofnewyork.us/api/views/7isb-wh4c/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/acris-document-control-codes/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/acris-document-control-codes/data.csv"]
