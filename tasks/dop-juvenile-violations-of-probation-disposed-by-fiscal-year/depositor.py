import requests
r = requests.get("https://data.cityofnewyork.us/api/views/gi3h-3i8t/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-violations-of-probation-disposed-by-fiscal-year/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-violations-of-probation-disposed-by-fiscal-year/data.csv"]
