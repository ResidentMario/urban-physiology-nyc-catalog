import requests
r = requests.get("https://data.cityofnewyork.us/api/views/niy5-4j7q/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-cooperative-comparable-rental-income-manhattan-fy-20092010/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-cooperative-comparable-rental-income-manhattan-fy-20092010/data.csv"]
