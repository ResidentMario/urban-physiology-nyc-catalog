import requests
r = requests.get("https://data.cityofnewyork.us/api/views/hii3-dcun/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/additional-revenue/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/additional-revenue/data.csv"]
