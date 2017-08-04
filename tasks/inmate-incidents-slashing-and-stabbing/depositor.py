import requests
r = requests.get("https://data.cityofnewyork.us/api/views/gakf-suji/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inmate-incidents-slashing-and-stabbing/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inmate-incidents-slashing-and-stabbing/data.csv"]
