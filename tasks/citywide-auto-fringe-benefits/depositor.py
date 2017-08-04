import requests
r = requests.get("https://data.cityofnewyork.us/api/views/8k4x-9mp5/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/citywide-auto-fringe-benefits/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/citywide-auto-fringe-benefits/data.csv"]
