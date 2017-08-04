import requests
r = requests.get("https://data.cityofnewyork.us/api/views/a9es-3fcm/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/family-planning-benefit-program-income-levels/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/family-planning-benefit-program-income-levels/data.csv"]
