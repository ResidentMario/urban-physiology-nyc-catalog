import requests
r = requests.get("https://data.cityofnewyork.us/api/views/8dhd-zvi6/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2001-campaign-payments/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2001-campaign-payments/data.csv"]
