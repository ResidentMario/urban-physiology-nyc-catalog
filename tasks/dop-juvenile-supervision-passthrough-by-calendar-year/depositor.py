import requests
r = requests.get("https://data.cityofnewyork.us/api/views/6r8r-c474/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-supervision-passthrough-by-calendar-year/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-supervision-passthrough-by-calendar-year/data.csv"]
