import requests
r = requests.get("https://data.cityofnewyork.us/api/views/4nft-bihw/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/assessment-actions/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/assessment-actions/data.csv"]
