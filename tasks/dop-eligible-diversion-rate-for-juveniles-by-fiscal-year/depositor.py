import requests
r = requests.get("https://data.cityofnewyork.us/api/views/cxcv-mgtn/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-eligible-diversion-rate-for-juveniles-by-fiscal-year/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-eligible-diversion-rate-for-juveniles-by-fiscal-year/data.csv"]
