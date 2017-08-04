import requests
r = requests.get("https://data.cityofnewyork.us/api/views/5jat-czce/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/topographical-bureau-maps/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/topographical-bureau-maps/data.csv"]
