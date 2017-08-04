import requests
r = requests.get("https://data.cityofnewyork.us/api/views/weg5-33pj/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-progress-report-2006-2007/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-progress-report-2006-2007/data.csv"]
