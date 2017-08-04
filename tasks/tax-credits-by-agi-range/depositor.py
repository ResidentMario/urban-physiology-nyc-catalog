import requests
r = requests.get("https://data.cityofnewyork.us/api/views/nwet-nc6h/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/tax-credits-by-agi-range/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/tax-credits-by-agi-range/data.csv"]
