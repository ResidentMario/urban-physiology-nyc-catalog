import requests
r = requests.get("https://data.cityofnewyork.us/api/views/3ups-txji/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/small-purchase-report/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/small-purchase-report/data.csv"]
