import requests
r = requests.get("https://data.cityofnewyork.us/api/views/9sys-2i9y/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-violations-of-probation-disposed-by-fiscal-year/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-violations-of-probation-disposed-by-fiscal-year/data.csv"]
