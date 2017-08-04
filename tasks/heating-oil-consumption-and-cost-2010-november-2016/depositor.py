import requests
r = requests.get("https://data.cityofnewyork.us/api/views/bhwu-wuzu/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/heating-oil-consumption-and-cost-2010-november-2016/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/heating-oil-consumption-and-cost-2010-november-2016/data.csv"]
