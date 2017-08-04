import requests
r = requests.get("https://data.cityofnewyork.us/api/views/hukm-snmq/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-independent-budget-office-ibo-capital-expenditures-since-1985/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-independent-budget-office-ibo-capital-expenditures-since-1985/data.csv"]
