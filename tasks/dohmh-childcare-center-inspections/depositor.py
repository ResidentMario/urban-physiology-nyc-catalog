import requests
r = requests.get("https://data.cityofnewyork.us/api/views/dsg6-ifza/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dohmh-childcare-center-inspections/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/dohmh-childcare-center-inspections/data.csv"]
