import requests
r = requests.get("https://data.cityofnewyork.us/api/views/tkdy-59zg/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-condominium-comparable-rental-income-staten-island-fy-20112012/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-condominium-comparable-rental-income-staten-island-fy-20112012/data.csv"]
