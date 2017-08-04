import requests
r = requests.get("https://data.cityofnewyork.us/api/views/nja7-3m37/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/strategic-plan-progress-report/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/strategic-plan-progress-report/data.csv"]
