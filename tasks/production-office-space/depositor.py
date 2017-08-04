import requests
r = requests.get("https://data.cityofnewyork.us/api/views/bvna-6j7v/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/production-office-space/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/production-office-space/data.csv"]
