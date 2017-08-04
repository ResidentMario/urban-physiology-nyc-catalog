import requests
r = requests.get("https://data.cityofnewyork.us/api/views/5fn4-dr26/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/charges/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/charges/data.csv"]
