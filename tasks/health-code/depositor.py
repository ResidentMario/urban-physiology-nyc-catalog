import requests
r = requests.get("https://data.cityofnewyork.us/api/views/3v48-95hb/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/health-code/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/health-code/data.csv"]
