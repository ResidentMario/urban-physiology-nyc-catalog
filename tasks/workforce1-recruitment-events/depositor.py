import requests
r = requests.get("https://data.cityofnewyork.us/api/views/kf2b-aeh5/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/workforce1-recruitment-events/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/workforce1-recruitment-events/data.csv"]
