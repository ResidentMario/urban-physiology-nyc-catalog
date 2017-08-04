import requests
r = requests.get("https://data.cityofnewyork.us/api/views/xnpc-vebg/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-discourtesy-allegations-2007/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-discourtesy-allegations-2007/data.csv"]
