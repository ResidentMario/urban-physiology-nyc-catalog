import requests
r = requests.get("https://data.cityofnewyork.us/api/views/tyfh-9h2y/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-cooperative-comparable-rental-income-brooklyn-fy-20092010/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dof-cooperative-comparable-rental-income-brooklyn-fy-20092010/data.csv"]
