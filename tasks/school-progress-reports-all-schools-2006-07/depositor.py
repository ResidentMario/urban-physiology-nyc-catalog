import requests
r = requests.get("https://data.cityofnewyork.us/api/views/fzv4-jan3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-progress-reports-all-schools-2006-07/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-progress-reports-all-schools-2006-07/data.csv"]
