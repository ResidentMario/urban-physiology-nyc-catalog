import requests
r = requests.get("https://data.cityofnewyork.us/api/views/hdnu-nbrh/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-independent-budget-office-ibo-tax-revenue-fy-1980-fy-2014/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-independent-budget-office-ibo-tax-revenue-fy-1980-fy-2014/data.csv"]
