import requests
r = requests.get("https://data.cityofnewyork.us/api/views/cw8b-zbc3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/tlc-vehicle-insurance/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/tlc-vehicle-insurance/data.csv"]
