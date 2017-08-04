import requests
r = requests.get("https://data.cityofnewyork.us/api/views/kyad-zm4j/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/1995-street-tree-census/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/1995-street-tree-census/data.csv"]
