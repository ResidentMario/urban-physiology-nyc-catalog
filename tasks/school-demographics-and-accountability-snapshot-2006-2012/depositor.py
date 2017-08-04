import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ihfw-zy9j/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-demographics-and-accountability-snapshot-2006-2012/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/school-demographics-and-accountability-snapshot-2006-2012/data.csv"]
