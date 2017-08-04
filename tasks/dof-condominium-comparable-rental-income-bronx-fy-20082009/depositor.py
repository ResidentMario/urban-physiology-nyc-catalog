import requests
r = requests.get("https://data.cityofnewyork.us/api/views/en2c-j6tw/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-condominium-comparable-rental-income-bronx-fy-20082009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-condominium-comparable-rental-income-bronx-fy-20082009/data.csv"]
