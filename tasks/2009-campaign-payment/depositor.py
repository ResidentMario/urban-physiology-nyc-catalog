import requests
r = requests.get("https://data.cityofnewyork.us/api/views/vyxt-abab/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2009-campaign-payment/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2009-campaign-payment/data.csv"]
