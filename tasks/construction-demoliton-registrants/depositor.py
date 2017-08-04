import requests
r = requests.get("https://data.cityofnewyork.us/api/views/cspg-yi7g/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/construction-demoliton-registrants/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/construction-demoliton-registrants/data.csv"]
