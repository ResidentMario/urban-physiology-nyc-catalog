import requests
r = requests.get("https://data.cityofnewyork.us/api/views/qt67-786k/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/medicaid-buy-in-program-income-levels/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/medicaid-buy-in-program-income-levels/data.csv"]
