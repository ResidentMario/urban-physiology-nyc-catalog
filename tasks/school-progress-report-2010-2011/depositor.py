import requests
r = requests.get("https://data.cityofnewyork.us/api/views/upwt-zvh3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-progress-report-2010-2011/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-progress-report-2010-2011/data.csv"]
