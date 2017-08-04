import requests
r = requests.get("https://data.cityofnewyork.us/api/views/aiww-p3af/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/311-service-requests-for-2007/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/311-service-requests-for-2007/data.csv"]
