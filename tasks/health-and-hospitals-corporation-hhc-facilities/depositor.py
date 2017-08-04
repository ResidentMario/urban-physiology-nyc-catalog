import requests
r = requests.get("https://data.cityofnewyork.us/api/views/f7b6-v6v3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/health-and-hospitals-corporation-hhc-facilities/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/health-and-hospitals-corporation-hhc-facilities/data.csv"]
