import requests
r = requests.get("https://data.cityofnewyork.us/api/views/m4pf-wpkz/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/trained-medallion-drivers/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/trained-medallion-drivers/data.csv"]
