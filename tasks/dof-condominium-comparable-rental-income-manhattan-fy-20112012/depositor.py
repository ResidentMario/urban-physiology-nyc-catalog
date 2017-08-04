import requests
r = requests.get("https://data.cityofnewyork.us/api/views/dvzp-h4k9/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-condominium-comparable-rental-income-manhattan-fy-20112012/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-condominium-comparable-rental-income-manhattan-fy-20112012/data.csv"]
