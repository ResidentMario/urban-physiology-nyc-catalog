import requests
r = requests.get("https://data.cityofnewyork.us/api/views/qj9s-yv6v/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/odra-ma-trend/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/odra-ma-trend/data.csv"]
