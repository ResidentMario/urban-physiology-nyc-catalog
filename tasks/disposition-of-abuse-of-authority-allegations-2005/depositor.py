import requests
r = requests.get("https://data.cityofnewyork.us/api/views/qf2v-7dbv/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-abuse-of-authority-allegations-2005/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/disposition-of-abuse-of-authority-allegations-2005/data.csv"]
