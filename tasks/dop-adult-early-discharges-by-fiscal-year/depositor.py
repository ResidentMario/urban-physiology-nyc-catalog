import requests
r = requests.get("https://data.cityofnewyork.us/api/views/4e8h-wu86/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-early-discharges-by-fiscal-year/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-early-discharges-by-fiscal-year/data.csv"]
