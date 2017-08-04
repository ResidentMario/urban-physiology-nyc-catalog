import requests
r = requests.get("https://data.cityofnewyork.us/api/views/az65-9z36/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-supervision-intakes-by-calendar-year/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-supervision-intakes-by-calendar-year/data.csv"]
