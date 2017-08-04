import requests
r = requests.get("https://data.cityofnewyork.us/api/views/vrn4-2abs/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-progress-report-2008-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-progress-report-2008-2009/data.csv"]
