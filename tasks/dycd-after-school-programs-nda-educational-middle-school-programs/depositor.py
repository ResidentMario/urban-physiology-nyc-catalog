import requests
r = requests.get("https://data.cityofnewyork.us/api/views/6rg9-pfbz/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-nda-educational-middle-school-programs/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dycd-after-school-programs-nda-educational-middle-school-programs/data.csv"]
