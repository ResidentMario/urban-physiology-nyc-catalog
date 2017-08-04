import requests
r = requests.get("https://data.cityofnewyork.us/api/views/9vgt-yx2p/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hydrostats/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/hydrostats/data.csv"]
