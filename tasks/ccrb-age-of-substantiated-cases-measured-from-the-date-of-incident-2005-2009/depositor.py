import requests
r = requests.get("https://data.cityofnewyork.us/api/views/jgjk-h2bn/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-age-of-substantiated-cases-measured-from-the-date-of-incident-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-age-of-substantiated-cases-measured-from-the-date-of-incident-2005-2009/data.csv"]
