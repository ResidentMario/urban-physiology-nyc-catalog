import requests
r = requests.get("https://data.cityofnewyork.us/api/views/i7jz-e2db/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/summary-table-of-funding-sources/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/summary-table-of-funding-sources/data.csv"]
