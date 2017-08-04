import requests
r = requests.get("https://data.cityofnewyork.us/api/views/bdjm-n7q4/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/forestry-work-orders/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/forestry-work-orders/data.csv"]
