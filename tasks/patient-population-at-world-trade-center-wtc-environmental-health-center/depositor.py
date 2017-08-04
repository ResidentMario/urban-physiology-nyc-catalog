import requests
r = requests.get("https://data.cityofnewyork.us/api/views/y4yc-78a4/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/patient-population-at-world-trade-center-wtc-environmental-health-center/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/patient-population-at-world-trade-center-wtc-environmental-health-center/data.csv"]
