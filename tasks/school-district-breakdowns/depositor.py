import requests
r = requests.get("https://data.cityofnewyork.us/api/views/g3vh-kbnw/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-district-breakdowns/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-district-breakdowns/data.csv"]
