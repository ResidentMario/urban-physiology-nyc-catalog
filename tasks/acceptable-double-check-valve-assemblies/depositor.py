import requests
r = requests.get("https://data.cityofnewyork.us/api/views/5e35-afph/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/acceptable-double-check-valve-assemblies/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/acceptable-double-check-valve-assemblies/data.csv"]
