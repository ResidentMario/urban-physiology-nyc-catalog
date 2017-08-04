import requests
r = requests.get("https://data.cityofnewyork.us/api/views/j2iz-mwzu/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/acris-country-codes/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/acris-country-codes/data.csv"]
