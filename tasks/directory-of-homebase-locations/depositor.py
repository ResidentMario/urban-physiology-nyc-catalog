import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ntcm-2w4k/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-homebase-locations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-homebase-locations/data.csv"]
