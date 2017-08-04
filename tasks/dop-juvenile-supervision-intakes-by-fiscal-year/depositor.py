import requests
r = requests.get("https://data.cityofnewyork.us/api/views/xdqu-utzq/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-supervision-intakes-by-fiscal-year/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-supervision-intakes-by-fiscal-year/data.csv"]
