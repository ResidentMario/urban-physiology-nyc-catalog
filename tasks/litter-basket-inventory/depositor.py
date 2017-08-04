import requests
r = requests.get("https://data.cityofnewyork.us/api/views/es7t-6u8y/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/litter-basket-inventory/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/litter-basket-inventory/data.csv"]
