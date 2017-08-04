import requests
r = requests.get("https://data.cityofnewyork.us/api/views/69w5-fdhb/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/justice-scholars-organization-information/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/justice-scholars-organization-information/data.csv"]
