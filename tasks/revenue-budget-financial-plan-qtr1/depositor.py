import requests
r = requests.get("https://data.cityofnewyork.us/api/views/vf4p-p8ui/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/revenue-budget-financial-plan-qtr1/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/revenue-budget-financial-plan-qtr1/data.csv"]
