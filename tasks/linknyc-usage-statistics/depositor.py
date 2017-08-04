import requests
r = requests.get("https://data.cityofnewyork.us/api/views/69wu-b929/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/linknyc-usage-statistics/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/linknyc-usage-statistics/data.csv"]
