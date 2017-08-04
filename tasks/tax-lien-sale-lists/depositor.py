import requests
r = requests.get("https://data.cityofnewyork.us/api/views/9rz4-mjek/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/tax-lien-sale-lists/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/tax-lien-sale-lists/data.csv"]
