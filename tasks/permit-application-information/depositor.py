import requests
r = requests.get("https://data.cityofnewyork.us/api/views/nj5b-z2hw/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/permit-application-information/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/permit-application-information/data.csv"]
