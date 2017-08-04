import requests
r = requests.get("https://data.cityofnewyork.us/api/views/99wq-x9cr/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-approved-tree-species-list/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-approved-tree-species-list/data.csv"]
