import requests
r = requests.get("https://data.cityofnewyork.us/api/views/65js-fhgz/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-cases-snapshot-by-calendar-year/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-cases-snapshot-by-calendar-year/data.csv"]
