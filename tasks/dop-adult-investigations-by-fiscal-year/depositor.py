import requests
r = requests.get("https://data.cityofnewyork.us/api/views/vvym-pu7g/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-investigations-by-fiscal-year/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-investigations-by-fiscal-year/data.csv"]
