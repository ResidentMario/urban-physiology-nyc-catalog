import requests
r = requests.get("https://data.cityofnewyork.us/api/views/3f5y-5web/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-supervision-passthrough-by-fiscal-year/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-supervision-passthrough-by-fiscal-year/data.csv"]
