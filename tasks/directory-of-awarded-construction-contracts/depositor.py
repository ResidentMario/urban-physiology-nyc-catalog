import requests
r = requests.get("https://data.cityofnewyork.us/api/views/j7gw-gcxi/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-awarded-construction-contracts/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-awarded-construction-contracts/data.csv"]
