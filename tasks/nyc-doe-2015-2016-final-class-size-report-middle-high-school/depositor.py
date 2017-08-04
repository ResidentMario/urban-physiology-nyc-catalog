import requests
r = requests.get("https://data.cityofnewyork.us/api/views/icps-nwdu/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-doe-2015-2016-final-class-size-report-middle-high-school/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-doe-2015-2016-final-class-size-report-middle-high-school/data.csv"]
