import requests
r = requests.get("https://data.cityofnewyork.us/api/views/jcih-dj9q/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-condominium-comparable-rental-income-queens-fy-20112012/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-condominium-comparable-rental-income-queens-fy-20112012/data.csv"]
