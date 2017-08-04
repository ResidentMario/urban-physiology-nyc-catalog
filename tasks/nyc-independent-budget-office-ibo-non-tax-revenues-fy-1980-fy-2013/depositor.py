import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ypbd-r4kg/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-independent-budget-office-ibo-non-tax-revenues-fy-1980-fy-2013/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-independent-budget-office-ibo-non-tax-revenues-fy-1980-fy-2013/data.csv"]
