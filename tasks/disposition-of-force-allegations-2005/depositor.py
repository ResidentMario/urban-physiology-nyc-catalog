import requests
r = requests.get("https://data.cityofnewyork.us/api/views/9tth-ctyd/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-force-allegations-2005/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-force-allegations-2005/data.csv"]
