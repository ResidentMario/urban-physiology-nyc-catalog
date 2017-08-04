import requests
r = requests.get("https://data.cityofnewyork.us/api/views/q7ra-ebu4/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/underutilized-space-report/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/underutilized-space-report/data.csv"]
