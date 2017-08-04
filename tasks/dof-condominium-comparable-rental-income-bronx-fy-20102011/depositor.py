import requests
r = requests.get("https://data.cityofnewyork.us/api/views/bawj-6bgn/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-condominium-comparable-rental-income-bronx-fy-20102011/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-condominium-comparable-rental-income-bronx-fy-20102011/data.csv"]
