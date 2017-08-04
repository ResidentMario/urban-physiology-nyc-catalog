import requests
r = requests.get("https://data.cityofnewyork.us/api/views/4n2j-ut8i/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-progress-report-2009-2010/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-progress-report-2009-2010/data.csv"]
