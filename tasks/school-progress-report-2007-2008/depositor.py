import requests
r = requests.get("https://data.cityofnewyork.us/api/views/yayv-apxh/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-progress-report-2007-2008/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-progress-report-2007-2008/data.csv"]
