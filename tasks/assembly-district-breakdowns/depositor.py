import requests
r = requests.get("https://data.cityofnewyork.us/api/views/2t32-hbca/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/assembly-district-breakdowns/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/assembly-district-breakdowns/data.csv"]
