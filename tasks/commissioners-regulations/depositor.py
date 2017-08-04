import requests
r = requests.get("https://data.cityofnewyork.us/api/views/a6x3-4y2a/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/commissioners-regulations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/commissioners-regulations/data.csv"]
