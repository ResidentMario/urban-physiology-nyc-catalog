import requests
r = requests.get("https://data.cityofnewyork.us/api/views/k2ye-5mmh/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-violations-of-probation-filed-by-calendar-year/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-violations-of-probation-filed-by-calendar-year/data.csv"]
