import requests
r = requests.get("https://data.cityofnewyork.us/api/views/45i5-r9tu/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-monitoring-data/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-monitoring-data/data.csv"]
