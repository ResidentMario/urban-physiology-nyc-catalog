import requests
r = requests.get("https://data.cityofnewyork.us/api/views/yig9-9zum/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-progress-reports-all-schools-2010-11/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-progress-reports-all-schools-2010-11/data.csv"]
