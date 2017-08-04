import requests
r = requests.get("https://data.cityofnewyork.us/api/views/x5tk-fa54/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/expense-financial-plan-exec/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/expense-financial-plan-exec/data.csv"]
