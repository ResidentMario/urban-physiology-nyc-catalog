import requests
r = requests.get("https://data.cityofnewyork.us/api/views/sapz-4gsi/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/approved-registrants-in-the-wholesale-markets/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/approved-registrants-in-the-wholesale-markets/data.csv"]
