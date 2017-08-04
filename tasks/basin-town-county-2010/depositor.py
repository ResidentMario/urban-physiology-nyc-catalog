import requests
r = requests.get("https://data.cityofnewyork.us/api/views/9akp-irxz/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/basin-town-county-2010/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/basin-town-county-2010/data.csv"]
