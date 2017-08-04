import requests
r = requests.get("https://data.cityofnewyork.us/api/views/yksz-5xaj/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/tlc-commuter-van-authorizations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/tlc-commuter-van-authorizations/data.csv"]
