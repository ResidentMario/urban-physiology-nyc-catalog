import requests
r = requests.get("https://data.cityofnewyork.us/api/views/qf92-qkjm/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-violations-of-probation-disposed-by-calendar-year/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-violations-of-probation-disposed-by-calendar-year/data.csv"]
