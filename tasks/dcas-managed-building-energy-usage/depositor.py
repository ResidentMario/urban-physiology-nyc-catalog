import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ubdi-jgw2/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dcas-managed-building-energy-usage/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dcas-managed-building-energy-usage/data.csv"]
