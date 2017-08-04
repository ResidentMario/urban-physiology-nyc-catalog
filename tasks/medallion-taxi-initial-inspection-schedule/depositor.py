import requests
r = requests.get("https://data.cityofnewyork.us/api/views/k2tc-bipg/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/medallion-taxi-initial-inspection-schedule/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/medallion-taxi-initial-inspection-schedule/data.csv"]
