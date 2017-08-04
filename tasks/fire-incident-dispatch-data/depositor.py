import requests
r = requests.get("https://data.cityofnewyork.us/api/views/8m42-w767/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fire-incident-dispatch-data/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fire-incident-dispatch-data/data.csv"]
