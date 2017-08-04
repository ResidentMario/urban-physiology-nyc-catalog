import requests
r = requests.get("https://data.cityofnewyork.us/api/views/a6nj-cfbz/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/wirednyc-all-buildings-data/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/wirednyc-all-buildings-data/data.csv"]
