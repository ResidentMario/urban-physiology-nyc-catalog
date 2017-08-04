import requests
r = requests.get("https://data.cityofnewyork.us/api/views/hn5i-inap/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/forestry-tree-points/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/forestry-tree-points/data.csv"]
