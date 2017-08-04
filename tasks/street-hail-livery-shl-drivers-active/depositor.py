import requests
r = requests.get("https://data.cityofnewyork.us/api/views/5tub-eh45/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/street-hail-livery-shl-drivers-active/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/street-hail-livery-shl-drivers-active/data.csv"]
