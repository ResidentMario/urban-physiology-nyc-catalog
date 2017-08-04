import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ugzk-a6x4/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/revenue-budget-financial-plan-execadptprel/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/revenue-budget-financial-plan-execadptprel/data.csv"]
