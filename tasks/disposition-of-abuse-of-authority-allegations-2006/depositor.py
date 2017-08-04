import requests
r = requests.get("https://data.cityofnewyork.us/api/views/b3wh-m425/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-abuse-of-authority-allegations-2006/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-abuse-of-authority-allegations-2006/data.csv"]
