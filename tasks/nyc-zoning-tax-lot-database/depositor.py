import requests
r = requests.get("https://data.cityofnewyork.us/api/views/fdkv-4t4z/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-zoning-tax-lot-database/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-zoning-tax-lot-database/data.csv"]
