import requests
r = requests.get("https://data.cityofnewyork.us/api/views/yrf7-4wry/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-cooperative-comparable-rental-income-bronx-fy-20112012/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-cooperative-comparable-rental-income-bronx-fy-20112012/data.csv"]
