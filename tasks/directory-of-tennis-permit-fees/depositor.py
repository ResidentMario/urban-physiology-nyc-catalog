import requests
r = requests.get("https://data.cityofnewyork.us/api/views/9n2n-hkug/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-tennis-permit-fees/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-tennis-permit-fees/data.csv"]
