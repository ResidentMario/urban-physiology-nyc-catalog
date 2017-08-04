import requests
r = requests.get("https://data.cityofnewyork.us/api/views/d84z-5kap/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/law-published-columns/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/law-published-columns/data.csv"]
