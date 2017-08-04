import requests
r = requests.get("https://data.cityofnewyork.us/api/views/8g9r-zz89/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/distribution-of-discourtesy-allegations-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/distribution-of-discourtesy-allegations-2005-2009/data.csv"]
