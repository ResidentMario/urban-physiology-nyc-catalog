import requests
r = requests.get("https://data.cityofnewyork.us/api/views/my4g-bvvs/rows.csv?accessType=DOWNLOAD")
with open("/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/enrollment-capacity-and-utilization-reports-district-1-32/data.csv", "wb") as f:
    f.write(r.content)

outputs = ["/home/alex/Desktop/urban-physiology-nyc-catalog/catalog/enrollment-capacity-and-utilization-reports-district-1-32/data.csv"]
