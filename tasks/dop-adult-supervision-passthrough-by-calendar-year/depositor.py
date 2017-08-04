import requests
r = requests.get("https://data.cityofnewyork.us/api/views/3av7-txd8/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-supervision-passthrough-by-calendar-year/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-supervision-passthrough-by-calendar-year/data.csv"]
