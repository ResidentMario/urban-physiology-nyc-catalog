import requests
r = requests.get("https://data.cityofnewyork.us/api/views/kcgr-4dqx/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-abuse-of-authority-allegations-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-abuse-of-authority-allegations-2009/data.csv"]
