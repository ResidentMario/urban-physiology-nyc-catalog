import requests
r = requests.get("https://data.cityofnewyork.us/api/views/qc6h-hbw3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-force-allegations-2007/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-force-allegations-2007/data.csv"]
