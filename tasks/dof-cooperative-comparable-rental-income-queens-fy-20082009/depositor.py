import requests
r = requests.get("https://data.cityofnewyork.us/api/views/cwg5-cqkm/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-cooperative-comparable-rental-income-queens-fy-20082009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-cooperative-comparable-rental-income-queens-fy-20082009/data.csv"]
