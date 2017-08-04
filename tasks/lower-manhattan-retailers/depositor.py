import requests
r = requests.get("https://data.cityofnewyork.us/api/views/cw88-qpsr/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/lower-manhattan-retailers/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/lower-manhattan-retailers/data.csv"]
