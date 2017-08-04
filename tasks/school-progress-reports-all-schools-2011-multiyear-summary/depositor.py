import requests
r = requests.get("https://data.cityofnewyork.us/api/views/rwa3-b3wr/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-progress-reports-all-schools-2011-multiyear-summary/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-progress-reports-all-schools-2011-multiyear-summary/data.csv"]
