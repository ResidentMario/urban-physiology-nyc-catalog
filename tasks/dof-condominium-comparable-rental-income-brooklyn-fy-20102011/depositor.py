import requests
r = requests.get("https://data.cityofnewyork.us/api/views/5mw2-hzqx/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-condominium-comparable-rental-income-brooklyn-fy-20102011/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-condominium-comparable-rental-income-brooklyn-fy-20102011/data.csv"]
