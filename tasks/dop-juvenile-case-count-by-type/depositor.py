import requests
r = requests.get("https://data.cityofnewyork.us/api/views/c49b-3kmd/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-case-count-by-type/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-juvenile-case-count-by-type/data.csv"]
