import requests
r = requests.get("https://data.cityofnewyork.us/api/views/b7kx-qikm/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2012-nyc-farmers-market-list/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2012-nyc-farmers-market-list/data.csv"]
