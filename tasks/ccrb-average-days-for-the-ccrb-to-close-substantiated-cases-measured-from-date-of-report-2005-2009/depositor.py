import requests
r = requests.get("https://data.cityofnewyork.us/api/views/bws2-q2sb/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-average-days-for-the-ccrb-to-close-substantiated-cases-measured-from-date-of-report-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-average-days-for-the-ccrb-to-close-substantiated-cases-measured-from-date-of-report-2005-2009/data.csv"]
