import requests
r = requests.get("https://data.cityofnewyork.us/api/views/rfpq-hs49/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-attendance-and-enrollment-by-district-2010-11/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-attendance-and-enrollment-by-district-2010-11/data.csv"]
