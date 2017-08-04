import requests
r = requests.get("https://data.cityofnewyork.us/api/views/vuae-w6cg/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/pmmr-2014-raw-data/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/pmmr-2014-raw-data/data.csv"]
