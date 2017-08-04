import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ii73-cgb4/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-discourtesy-allegations-2008/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-discourtesy-allegations-2008/data.csv"]
