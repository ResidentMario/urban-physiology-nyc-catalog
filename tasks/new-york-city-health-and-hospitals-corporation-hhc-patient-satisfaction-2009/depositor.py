import requests
r = requests.get("https://data.cityofnewyork.us/api/views/hi3x-y76v/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-health-and-hospitals-corporation-hhc-patient-satisfaction-2009/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/new-york-city-health-and-hospitals-corporation-hhc-patient-satisfaction-2009/data.csv"]
