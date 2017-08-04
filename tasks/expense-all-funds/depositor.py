import requests
r = requests.get("https://data.cityofnewyork.us/api/views/am45-6syq/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/expense-all-funds/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/expense-all-funds/data.csv"]
