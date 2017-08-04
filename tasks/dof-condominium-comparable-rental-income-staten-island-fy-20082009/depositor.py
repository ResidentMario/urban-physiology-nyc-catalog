import requests
r = requests.get("https://data.cityofnewyork.us/api/views/cyfw-hfqk/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-condominium-comparable-rental-income-staten-island-fy-20082009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-condominium-comparable-rental-income-staten-island-fy-20082009/data.csv"]
