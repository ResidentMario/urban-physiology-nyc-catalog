import requests
r = requests.get("https://data.cityofnewyork.us/api/views/7r8u-zrb7/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/firearms-discharge-report/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/firearms-discharge-report/data.csv"]
