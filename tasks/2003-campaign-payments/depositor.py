import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ms66-xjfq/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2003-campaign-payments/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2003-campaign-payments/data.csv"]
