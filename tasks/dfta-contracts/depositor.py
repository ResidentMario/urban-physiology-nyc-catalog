import requests
r = requests.get("https://data.cityofnewyork.us/api/views/6j6t-3ixh/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dfta-contracts/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dfta-contracts/data.csv"]
