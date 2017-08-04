import requests
r = requests.get("https://data.cityofnewyork.us/api/views/g8v5-qeu5/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-age-of-docket-measured-from-the-date-of-incident-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-age-of-docket-measured-from-the-date-of-incident-2005-2009/data.csv"]
