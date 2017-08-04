import requests
r = requests.get("https://data.cityofnewyork.us/api/views/yhuu-4pt3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/street-hail-livery-shl-permits/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/street-hail-livery-shl-permits/data.csv"]
