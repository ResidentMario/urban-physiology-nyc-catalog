import requests
r = requests.get("https://data.cityofnewyork.us/api/views/gaq9-z3hz/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/recycling-diversion-and-capture-rates/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/recycling-diversion-and-capture-rates/data.csv"]
