import requests
r = requests.get("https://data.cityofnewyork.us/api/views/r4c5-ndkx/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/lot-cleaning-dispositions/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/lot-cleaning-dispositions/data.csv"]
