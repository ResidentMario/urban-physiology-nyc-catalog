import requests
r = requests.get("https://data.cityofnewyork.us/api/views/66be-66yr/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/water-consumption-and-cost-2013-2016/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/water-consumption-and-cost-2013-2016/data.csv"]
