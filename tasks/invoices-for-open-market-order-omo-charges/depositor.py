import requests
r = requests.get("https://data.cityofnewyork.us/api/views/emrz-5p35/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/invoices-for-open-market-order-omo-charges/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/invoices-for-open-market-order-omo-charges/data.csv"]
