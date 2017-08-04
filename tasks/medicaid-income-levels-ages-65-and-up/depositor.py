import requests
r = requests.get("https://data.cityofnewyork.us/api/views/dn64-92ub/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/medicaid-income-levels-ages-65-and-up/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/medicaid-income-levels-ages-65-and-up/data.csv"]
