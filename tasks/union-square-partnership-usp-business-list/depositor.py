import requests
r = requests.get("https://data.cityofnewyork.us/api/views/p6bh-gqsg/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/union-square-partnership-usp-business-list/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/union-square-partnership-usp-business-list/data.csv"]
