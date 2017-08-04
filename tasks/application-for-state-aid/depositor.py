import requests
r = requests.get("https://data.cityofnewyork.us/api/views/8gpu-s594/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/application-for-state-aid/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/application-for-state-aid/data.csv"]
