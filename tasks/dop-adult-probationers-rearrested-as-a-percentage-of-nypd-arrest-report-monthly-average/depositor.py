import requests
r = requests.get("https://data.cityofnewyork.us/api/views/arhf-esqb/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-probationers-rearrested-as-a-percentage-of-nypd-arrest-report-monthly-average/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dop-adult-probationers-rearrested-as-a-percentage-of-nypd-arrest-report-monthly-average/data.csv"]
