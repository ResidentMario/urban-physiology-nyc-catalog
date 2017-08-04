import requests
r = requests.get("https://data.cityofnewyork.us/api/views/rnsn-acs2/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/census-demographics-at-the-neighborhood-tabulation-area-nta-level/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/census-demographics-at-the-neighborhood-tabulation-area-nta-level/data.csv"]
