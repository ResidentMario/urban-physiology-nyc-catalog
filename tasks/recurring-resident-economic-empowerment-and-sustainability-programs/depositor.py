import requests
r = requests.get("https://data.cityofnewyork.us/api/views/7su9-xgtn/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/recurring-resident-economic-empowerment-and-sustainability-programs/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/recurring-resident-economic-empowerment-and-sustainability-programs/data.csv"]
