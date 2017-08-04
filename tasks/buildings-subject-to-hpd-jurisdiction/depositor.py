import requests
r = requests.get("https://data.cityofnewyork.us/api/views/kj4p-ruqc/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/buildings-subject-to-hpd-jurisdiction/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/buildings-subject-to-hpd-jurisdiction/data.csv"]
