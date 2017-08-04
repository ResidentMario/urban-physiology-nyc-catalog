import requests
r = requests.get("https://data.cityofnewyork.us/api/views/erra-pzy8/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inmate-assault-on-staff/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/inmate-assault-on-staff/data.csv"]
