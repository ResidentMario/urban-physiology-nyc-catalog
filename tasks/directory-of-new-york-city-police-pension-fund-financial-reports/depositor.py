import requests
r = requests.get("https://data.cityofnewyork.us/api/views/e266-vpg7/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-new-york-city-police-pension-fund-financial-reports/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-new-york-city-police-pension-fund-financial-reports/data.csv"]
