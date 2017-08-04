import requests
r = requests.get("https://data.cityofnewyork.us/api/views/pvqr-7yc4/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/parking-violations-issued-fiscal-year-2017/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/parking-violations-issued-fiscal-year-2017/data.csv"]
