import requests
r = requests.get("https://data.cityofnewyork.us/api/views/9d9t-bmk7/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-job-centers/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/directory-of-job-centers/data.csv"]
