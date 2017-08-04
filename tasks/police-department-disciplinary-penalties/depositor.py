import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ns22-2dcm/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/police-department-disciplinary-penalties/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/police-department-disciplinary-penalties/data.csv"]
