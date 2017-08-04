import requests
r = requests.get("https://data.cityofnewyork.us/api/views/qgea-i56i/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nypd-complaint-data-historic/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nypd-complaint-data-historic/data.csv"]
