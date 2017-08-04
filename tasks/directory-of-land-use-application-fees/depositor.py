import requests
r = requests.get("https://data.cityofnewyork.us/api/views/fdx7-6jsr/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-land-use-application-fees/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-land-use-application-fees/data.csv"]
