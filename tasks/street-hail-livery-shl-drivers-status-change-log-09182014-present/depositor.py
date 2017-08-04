import requests
r = requests.get("https://data.cityofnewyork.us/api/views/v3mc-68jm/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/street-hail-livery-shl-drivers-status-change-log-09182014-present/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/street-hail-livery-shl-drivers-status-change-log-09182014-present/data.csv"]
