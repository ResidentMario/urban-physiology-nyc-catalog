import requests
r = requests.get("https://data.cityofnewyork.us/api/views/867j-5pgi/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/trade-waste-hauler-licensees/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/trade-waste-hauler-licensees/data.csv"]
