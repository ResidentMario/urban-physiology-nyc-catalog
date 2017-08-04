import requests
r = requests.get("https://data.cityofnewyork.us/api/views/mqd6-mvf7/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/incident-based-distribution-of-readyny-guides/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/incident-based-distribution-of-readyny-guides/data.csv"]
