import requests
r = requests.get("https://data.cityofnewyork.us/api/views/ay9k-vznm/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/workforce1-job-listing/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/workforce1-job-listing/data.csv"]
