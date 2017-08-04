import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ymvu-4x4s/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-domain-registrations-by-zip-code/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-domain-registrations-by-zip-code/data.csv"]
