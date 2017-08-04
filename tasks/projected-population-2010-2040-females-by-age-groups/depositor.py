import requests
r = requests.get("https://data.cityofnewyork.us/api/views/xxf6-krb6/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/projected-population-2010-2040-females-by-age-groups/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/projected-population-2010-2040-females-by-age-groups/data.csv"]
