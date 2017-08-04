import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ye26-g8nx/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/city-tax-revenue-financial-plan/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/city-tax-revenue-financial-plan/data.csv"]
