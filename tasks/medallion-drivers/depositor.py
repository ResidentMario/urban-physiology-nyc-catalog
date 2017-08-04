import requests
r = requests.get("https://data.cityofnewyork.us/api/views/iux8-53rc/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/medallion-drivers/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/medallion-drivers/data.csv"]
