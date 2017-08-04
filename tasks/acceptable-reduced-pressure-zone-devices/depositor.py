import requests
r = requests.get("https://data.cityofnewyork.us/api/views/iftc-eqzb/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/acceptable-reduced-pressure-zone-devices/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/acceptable-reduced-pressure-zone-devices/data.csv"]
