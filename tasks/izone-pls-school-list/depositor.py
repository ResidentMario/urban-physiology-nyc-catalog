import requests
r = requests.get("https://data.cityofnewyork.us/api/views/g993-cbry/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/izone-pls-school-list/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/izone-pls-school-list/data.csv"]
