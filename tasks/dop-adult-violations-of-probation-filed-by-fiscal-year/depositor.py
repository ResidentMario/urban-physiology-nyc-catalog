import requests
r = requests.get("https://data.cityofnewyork.us/api/views/fve3-eee8/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-violations-of-probation-filed-by-fiscal-year/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-violations-of-probation-filed-by-fiscal-year/data.csv"]
