import requests
r = requests.get("https://data.cityofnewyork.us/api/views/kpjg-ubxi/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/constituent-services/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/constituent-services/data.csv"]
