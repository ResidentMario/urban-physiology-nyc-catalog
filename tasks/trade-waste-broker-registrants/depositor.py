import requests
r = requests.get("https://data.cityofnewyork.us/api/views/krx7-u82t/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/trade-waste-broker-registrants/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/trade-waste-broker-registrants/data.csv"]
