import requests
r = requests.get("https://data.cityofnewyork.us/api/views/cwjy-rrh3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-independent-budget-office-ibo-agency-expenditures-fy-1980-2013/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-independent-budget-office-ibo-agency-expenditures-fy-1980-2013/data.csv"]
