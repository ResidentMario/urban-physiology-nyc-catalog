import requests
r = requests.get("https://data.cityofnewyork.us/api/views/niyd-ckq3/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-average-days-for-the-police-department-to-close-substantiated-ccrb-cases-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/ccrb-average-days-for-the-police-department-to-close-substantiated-ccrb-cases-2005-2009/data.csv"]
