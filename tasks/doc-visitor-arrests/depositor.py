import requests
r = requests.get("https://data.cityofnewyork.us/api/views/hm7r-w4y9/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doc-visitor-arrests/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/doc-visitor-arrests/data.csv"]
