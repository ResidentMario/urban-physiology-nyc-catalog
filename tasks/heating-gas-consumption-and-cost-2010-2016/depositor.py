import requests
r = requests.get("https://data.cityofnewyork.us/api/views/it56-eyq4/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/heating-gas-consumption-and-cost-2010-2016/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/heating-gas-consumption-and-cost-2010-2016/data.csv"]
