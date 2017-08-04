import requests
r = requests.get("https://data.cityofnewyork.us/api/views/8a4n-zmpj/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/art-in-doe-buildings/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/art-in-doe-buildings/data.csv"]
