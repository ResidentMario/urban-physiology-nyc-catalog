import requests
r = requests.get("https://data.cityofnewyork.us/api/views/4epu-t832/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-cases-snapshot-by-fiscal-year/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-cases-snapshot-by-fiscal-year/data.csv"]
