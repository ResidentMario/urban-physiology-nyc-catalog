import requests
r = requests.get("https://data.cityofnewyork.us/api/views/33c5-b922/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/summary-of-dbp-quarterly-report/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/summary-of-dbp-quarterly-report/data.csv"]
