import requests
r = requests.get("https://data.cityofnewyork.us/api/views/59t5-r7nb/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/foil-report-trade-waste-all-approved-or-denied/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/foil-report-trade-waste-all-approved-or-denied/data.csv"]
