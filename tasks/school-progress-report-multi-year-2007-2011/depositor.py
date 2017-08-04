import requests
r = requests.get("https://data.cityofnewyork.us/api/views/5fsg-d8c9/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-progress-report-multi-year-2007-2011/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-progress-report-multi-year-2007-2011/data.csv"]
