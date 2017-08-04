import requests
r = requests.get("https://data.cityofnewyork.us/api/views/k2zs-b24z/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-future-construction-projects/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-future-construction-projects/data.csv"]
