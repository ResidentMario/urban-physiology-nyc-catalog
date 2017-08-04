import requests
r = requests.get("https://data.cityofnewyork.us/api/views/2pmj-y4p4/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/audited-register-data/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/audited-register-data/data.csv"]
