import requests
r = requests.get("https://data.cityofnewyork.us/api/views/p32s-yqxq/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/historical-driver-application-status/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/historical-driver-application-status/data.csv"]
