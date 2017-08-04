import requests
r = requests.get("https://data.cityofnewyork.us/api/views/dgg9-jkx8/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/world-trade-center-wtc-patient-categories/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/world-trade-center-wtc-patient-categories/data.csv"]
