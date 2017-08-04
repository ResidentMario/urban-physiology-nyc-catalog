import requests
r = requests.get("https://data.cityofnewyork.us/api/views/y3gq-zv28/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-case-count-by-type/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-case-count-by-type/data.csv"]
