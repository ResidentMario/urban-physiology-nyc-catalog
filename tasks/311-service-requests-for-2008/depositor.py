import requests
r = requests.get("https://data.cityofnewyork.us/api/views/uzcy-9puk/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/311-service-requests-for-2008/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/311-service-requests-for-2008/data.csv"]
