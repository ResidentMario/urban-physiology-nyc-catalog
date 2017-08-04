import requests
r = requests.get("https://data.cityofnewyork.us/api/views/kwte-dppd/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-parks-daily-tasks-cleaning-records-fiscal-year-2016/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/nyc-parks-daily-tasks-cleaning-records-fiscal-year-2016/data.csv"]
