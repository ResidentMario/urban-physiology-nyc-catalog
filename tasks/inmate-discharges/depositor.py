import requests
r = requests.get("https://data.cityofnewyork.us/api/views/94ri-3ium/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inmate-discharges/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inmate-discharges/data.csv"]
