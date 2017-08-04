import requests
r = requests.get("https://data.cityofnewyork.us/api/views/tphb-2tdm/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/approved-licensees-and-registrants-for-trade-waste/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/approved-licensees-and-registrants-for-trade-waste/data.csv"]
