import requests
r = requests.get("https://data.cityofnewyork.us/api/views/9ct9-prf9/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ap-results/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ap-results/data.csv"]
