import requests
r = requests.get("https://data.cityofnewyork.us/api/views/jfzu-yy6n/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/oil-boilers-detailed-fuel-consumption-and-building-data/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/oil-boilers-detailed-fuel-consumption-and-building-data/data.csv"]
