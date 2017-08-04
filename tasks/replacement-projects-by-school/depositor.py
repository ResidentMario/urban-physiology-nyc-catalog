import requests
r = requests.get("https://data.cityofnewyork.us/api/views/kydh-ijhc/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/replacement-projects-by-school/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/replacement-projects-by-school/data.csv"]
