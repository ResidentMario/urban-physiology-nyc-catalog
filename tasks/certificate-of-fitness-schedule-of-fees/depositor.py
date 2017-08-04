import requests
r = requests.get("https://data.cityofnewyork.us/api/views/2ghx-qqsj/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/certificate-of-fitness-schedule-of-fees/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/certificate-of-fitness-schedule-of-fees/data.csv"]
