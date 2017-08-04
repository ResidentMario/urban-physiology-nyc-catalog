import requests
r = requests.get("https://data.cityofnewyork.us/api/views/xx2p-4jnq/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dcas-managed-public-buildings/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dcas-managed-public-buildings/data.csv"]
