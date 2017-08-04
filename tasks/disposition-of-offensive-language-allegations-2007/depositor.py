import requests
r = requests.get("https://data.cityofnewyork.us/api/views/xah7-gu5w/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-offensive-language-allegations-2007/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-offensive-language-allegations-2007/data.csv"]
