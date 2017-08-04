import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ph29-5mxy/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-cases-snapshot-by-calendar-year/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-cases-snapshot-by-calendar-year/data.csv"]
