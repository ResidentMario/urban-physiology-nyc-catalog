import requests
r = requests.get("https://data.cityofnewyork.us/api/views/2v9c-2k7f/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fhv-base-aggregate-report/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/fhv-base-aggregate-report/data.csv"]
