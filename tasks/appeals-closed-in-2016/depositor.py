import requests
r = requests.get("https://data.cityofnewyork.us/api/views/wbtw-zkex/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/appeals-closed-in-2016/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/appeals-closed-in-2016/data.csv"]
