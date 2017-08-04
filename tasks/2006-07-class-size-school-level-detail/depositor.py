import requests
r = requests.get("https://data.cityofnewyork.us/api/views/qfk7-6ens/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2006-07-class-size-school-level-detail/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/2006-07-class-size-school-level-detail/data.csv"]
