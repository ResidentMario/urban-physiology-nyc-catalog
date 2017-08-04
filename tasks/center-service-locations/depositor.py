import requests
r = requests.get("https://data.cityofnewyork.us/api/views/6smc-7mk6/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/center-service-locations/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/center-service-locations/data.csv"]
