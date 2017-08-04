import requests
r = requests.get("https://data.cityofnewyork.us/api/views/jr24-e7cr/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/electric-consumption-and-cost-2010-2016/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/electric-consumption-and-cost-2010-2016/data.csv"]
