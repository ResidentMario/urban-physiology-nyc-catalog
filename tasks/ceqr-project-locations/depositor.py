import requests
r = requests.get("https://data.cityofnewyork.us/api/views/did2-qzw3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ceqr-project-locations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ceqr-project-locations/data.csv"]
