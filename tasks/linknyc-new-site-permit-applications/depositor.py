import requests
r = requests.get("https://data.cityofnewyork.us/api/views/xp25-gxux/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/linknyc-new-site-permit-applications/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/linknyc-new-site-permit-applications/data.csv"]
