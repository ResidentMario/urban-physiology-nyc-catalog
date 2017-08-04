import requests
r = requests.get("https://data.cityofnewyork.us/api/views/jhq9-vaec/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/gender-of-subject-officers-compared-to-new-york-city-police-department-demographics-2005-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/gender-of-subject-officers-compared-to-new-york-city-police-department-demographics-2005-2009/data.csv"]
